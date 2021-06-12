from flask import Flask, render_template, url_for, request

from service import *

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
        if valid_login(request.form['email'], request.form['password']):
            return render_template('home.html')
        else:
            return render_template('error.html')
    else:
        return render_template('login.html')


@app.route("/signup", methods=['POST', 'GET'])
def signup():
    """Sign in page"""
    return "<h1>Sign Up Page<h1>"


@app.route("/add_new_person", methods=['POST'])
def add_new_person():
    """add new person page"""
    return "<h1>Add New Person Page<h1>"


@app.route("/get_table", methods=['GET'])
def get_table():
    """get table information"""
    return "<h1>Get Table Page<h1>"


@app.route("/get_tree", methods=['GET'])
def get_tree(token, name):
    """get tree information"""
    return get_tree_information(token, name)


if __name__ == "__main__":
    app.run()
