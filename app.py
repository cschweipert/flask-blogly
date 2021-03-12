"""Blogly application."""

from flask import Flask, render_template, request, redirect
from models import db, connect_db, User, Post
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

    users = User.query.all()
    return render_template("users.html", users=users)


@app.route("/users")
def show_users():
    """Shows all users"""

    users = User.query.all()
    return render_template("users.html", users=users)


@app.route("/users/new")
def add_user():
    """Show add user form"""

    return render_template("create_user.html")


@app.route("/users/new", methods=["POST"])
def process_form():
    """Add user and redirect to users"""

    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    img_url = request.form["img_url"] or None

    user = User(first_name=first_name, last_name=last_name, img_url=img_url)
    db.session.add(user)
    db.session.commit()

    # after post request => redirect
    return redirect("/users")


@app.route("/users/<int:user_id>")
def show_user(user_id):
    """Show details about a single user"""

    user = User.query.get_or_404(user_id)
    return render_template("detail.html", user=user)


@app.route("/users/<int:user_id>/edit")
def edit_user(user_id):
    """Edit single user"""

    user = User.query.get_or_404(user_id)
    return render_template("edit_user.html", user=user)


@app.route("/users/<int:user_id>/edit", methods=["POST"])
def process_edit_form(user_id):
    """Edit user"""

    user = User.query.get_or_404(user_id)

    user.first_name = request.form["first_name"]
    user.last_name = request.form["last_name"]
    user.img_url = request.form["img_url"] or None

    db.session.add(user)
    db.session.commit()

    return redirect("/users")


@app.route("/users/<int:user_id>/delete", methods=["POST"])
def delete_user(user_id):
    """Delete user"""

    user = User.query.get_or_404(user_id)

    db.session.delete(user)
    db.session.commit()

    return redirect("/users")


@app.route('/users/<int:user_id>/posts/new')
def posts_new_form(user_id):
    """Show new post form"""

    user = User.query.get_or_404(user_id)
    return render_template('create_post.html', user=user)


@app.route('/users/<int:user_id>/posts/new', methods=["POST"])
def create_post(user_id):
    """Create a new post"""

    user = User.query.get_or_404(user_id)

    title = request.form["title"]
    content = request.form["content"]

    post = Post(title=title, content=content, user_id=user_id)

    db.session.add(post)
    db.session.commit()

    return redirect(f"/users/{user_id}")


@app.route('/posts/<int:post_id>')
def show_posts(post_id):
    """Show post"""

    post = Post.query.get_or_404(post_id)
    return render_template('post.html', post=post)


@app.route('/posts/<int:post_id>/edit')
def posts_edit(post_id):
    """Show form to edit a post"""

    post = Post.query.get_or_404(post_id)
    return render_template('edit_post.html', post=post)


@app.route('/posts/<int:post_id>/edit', methods=["POST"])
def posts_update(post_id):
    """Updating a post"""

    post = Post.query.get_or_404(post_id)
    post.title = request.form['title']
    post.content = request.form['content']

    db.session.add(post)
    db.session.commit()

    return redirect(f"/users/{post.user_id}")


@app.route('/posts/<int:post_id>/delete', methods=["POST"])
def posts_destroy(post_id):
    """Delete a post"""

    post = Post.query.get_or_404(post_id)

    db.session.delete(post)
    db.session.commit()

    return redirect(f"/users/{post.user_id}")