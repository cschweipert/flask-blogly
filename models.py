"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class User(db.Model):
    """User."""

    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String(50),
                           nullable=False,
                           unique=True)
    last_name = db.Column(db.String(50),
                          nullable=False,
                          unique=True)
    img_url = db.Column(db.Text,
                          nullable=True,
                          default="https://icatcare.org/app/uploads/2018/06/Layer-1704-1920x840.jpg")
    db
    posts = db.relationship("Post")



class Post(db.Model):
    """Post."""

    __tablename__ = "posts"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    title = db.Column(db.String(100),
                        nullable=False,
                        unique=True)
    content = db.Column(db.Text,
                    nullable=False,
                    unique=True)
    created_at = db.Column(db.DateTime,
                    nullable=False,
                    unique=True),
    user_id = db.Column(db.Integer,
                    db.ForeignKey("users.id"),
                    nullable=False)
    user = db.relationship("User")
