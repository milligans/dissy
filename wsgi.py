from flask import Flask



app = Flask(__ name __)

@app.route('/')
def home_page():
    return 'Welcome, I bid you welcome'

