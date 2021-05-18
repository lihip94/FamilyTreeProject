from flask import Flask

app = Flask(__name__)


@app.route("/home")
def home():
    """Home page"""
    return "<h1>Home Page<h1>"


@app.route("/login")
def login():
    """Log in page"""
    return "<h1>Login Page<h1>"


@app.route("/signup")
def signup():
    """Sign in page"""
    return "<h1>Sign Up Page<h1>"


@app.route("/add_new_person")
def add_new_person():
    """add new person page"""
    return "<h1>Add New Person Page<h1>"


@app.route("/get_table")
def get_table():
    """get table information"""
    return "<h1>Get Table Page<h1>"


@app.route("/get_tree")
def get_tree():
    """get tree information"""
    return "<h1>Get Tree Page<h1>"


if __name__ == "__main__":
    app.run()