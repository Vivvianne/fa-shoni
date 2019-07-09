from . import main
from flask import render_template
# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to fa-shoni'


    return render_template('index.html', title=title)