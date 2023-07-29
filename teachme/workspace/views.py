from flask import render_template

def index(resources=None):
    return render_template('index.html', resources=resources)
