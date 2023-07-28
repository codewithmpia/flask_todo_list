from flask import render_template, request, redirect, url_for, flash

from .settings import app, db
from .models import Task

# All tasks
@app.route("/", methods=("GET", "POST"))
def todo_list():
    tasks = Task.query.order_by(Task.date.desc())
    page = request.args.get("page")

    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    tasks = tasks.paginate(page=page, per_page=10)
    return render_template("index.html", tasks=tasks)

# Show detail of task
@app.route("/todos/<int:todo_id>/")
def todo_detail(todo_id):
    task = Task.query.get_or_404(todo_id)
    return render_template("todo_detail.html", task=task)

# Add task
@app.route("/todos/create/", methods=("GET", "POST"))
def create_todo():
    if request.method == "POST":
        name = request.form.get("name")
        new_task = Task(name=name)
        db.session.add(new_task)
        db.session.commit()
        flash("La tâche a été ajouté avec succès.", "success")
        return redirect(url_for("todo_list"))
    
    return render_template("create_todo.html")

# Edit task
@app.route("/todos/edit/<int:todo_id>/", methods=("GET", "POST"))
def edit_todo(todo_id):
    task = Task.query.get_or_404(todo_id)

    if request.method == "POST":
        name = request.form.get("name")
        task.name = name
        db.session.commit()
        flash("La tâche a été modifiée avec succès.", "success")
        return redirect(url_for("todo_list"))
    
    return render_template("edit_todo.html", task=task)

# Delete task
@app.route("/todos/delete/<int:todo_id>/")
def delete_todo(todo_id):
    task = Task.query.get_or_404(todo_id)
    db.session.delete(task)
    db.session.commit()
    flash("La tâche a été supprimer avec succès.", "success")
    return redirect(url_for("todo_list"))