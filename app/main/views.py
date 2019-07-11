from flask import render_template
from . import main
# from ..requests import get_movies,get_movie,search_movie
# from .forms import ReviewForm,UpdateProfile
# from ..models import Review,User
# from flask_login import login_required, current_user
# from .. import db,photos




@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    
    title = 'Fa-shoni'

    return render_template('index.html', title = title )
