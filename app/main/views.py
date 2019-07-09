from flask import render_template
from app import app

@app.route('/')
def index():
    '''
    View the home page
    '''
    return render_template('women.html')
