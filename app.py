"""Blogly application."""

from flask import Flask, render_template, request, redirect
from models import db, connect_db
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)


@app.route("/")
def redirect_to_listings():
    """Redirect to listings page"""

    return render_template("listing.html")


@app.route("/users")
def show_users():
    """Shows all users"""

    return render_template("listing.html")


@app.route("/users/new")
def add_user():
    """Show add user form"""

    return render_template("create_user.html")


@app.route("/users/new", methods=["POST"])
def process_form():
    """Add user"""

    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    img_url = request.form["img_url"]

    return render_template("listing.html")


@app.route("/users/[user-id]")
def show_user():
    """Show details about single user"""

    return render_template("detail.html")


@app.route("/users/[user-id]/edit")
def edit_user():
    """Edit single user"""

    return render_template("edit_user.html")

# ToDo
@app.route("/users/[user-id]/edit", methods=["POST"])
def process_edit_form():
    """Edit user"""

    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    img_url = request.form["img_url"]

    return render_template("listing.html")

# ToDo
@app.route("/users/[user-id]/delete", methods=["POST"])
def delete_user():
    """Delete user"""

    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    img_url = request.form["img_url"]

    return render_template("listing.html")


