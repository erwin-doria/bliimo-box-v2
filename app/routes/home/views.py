from flask import render_template, request
from . import home
from app.controllers.HomeController import HomeController

@home.route('/', methods=['GET'])
def homepage():
        return render_template('home/index.html', title="Welcome")

@home.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
       return render_template('home/login.html', title="Login")

    elif request.method == 'POST': 
        credentials = request.json   
        return HomeController.login(credentials)