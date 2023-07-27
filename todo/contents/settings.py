from pathlib import Path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5

BASE_DIR = Path(__file__).resolve().parent.parent.parent

app = Flask(
    __name__,
    instance_path=BASE_DIR,
    template_folder=BASE_DIR / "todo/assets/templates",
    static_folder=BASE_DIR / "todo/assets/static"
)
# Secret Key
app.config["SECRET_KEY"] = "top-secret"

# Database
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{BASE_DIR}/db.sqlite3"
db = SQLAlchemy(app)

# Bootstrap
bootstrap = Bootstrap5(app)

# Views & Urls
from .import views

