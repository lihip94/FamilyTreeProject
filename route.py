from flask import Flask, render_template, url_for, request

import service

app = Flask(__name__)


@app.route("/")
def land():
    """Landing page"""
    return "<h1>Landing page<h1>"


@app.route("/home")
def home():
    """Home page"""
    return "<h1>Home Page<h1>"


@app.route("/login", methods=['POST', 'GET'])
def login():
    """Log in page"""
    if request.method == 'POST':
        return "<h1>Temp page - login<h1>"
    else:
        return render_template('login.html')


@app.route("/signup")
def signup():
    """Sign in page"""
    return "<h1>Sign Up Page<h1>"

# parm person , post/get
@app.route("/add_new_person")
def add_new_person():
    """add new person page"""
    return "<h1>Add New Person Page<h1>"


@app.route("/get_table")
def get_table():
    """get table information"""
    return "<h1>Get Table Page<h1>"


@app.route("/get_tree/<token>/<name>")
def get_tree(token, name):
    """get tree information"""
    return service.get_tree(token, name)


if __name__ == "__main__":
    app.run()
