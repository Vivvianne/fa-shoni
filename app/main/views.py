from flask import render_template,request,redirect,url_for
from . import main
from ..models import User,Subscription
from .. import db
from .forms import SubscriptionForm ,UpdateForm
from ..email import mail_message
from flask_login import login_user, logout_user, login_required



# Views
@main.route('/', methods=['GET', 'POST'])
def index():
    '''
    View root page function that returns the index page and its data
    '''

    form = SubscriptionForm()

    if form.validate_on_submit(): 
               
        new_subscription = Subscription(email=form.email.data)
        new_subscription.save_email()

    

    return render_template('index.html', SubscriptionForm = form)

# @main.route('/update/<name>', methods=['GET', 'POST'])
# @login_required
# def update():

#     form = UpdateForm()
    
    # if form.validate_on_submit():
    #     user = Profile(name =form.name.data, contact= form.contact.data, bio = form.bio.data, adress = form.location.data)
    #     db.session.add(user)
    #     db.session.commit()
    
    # if form.validate_on_submit():
    #     current_user.name = form.name.data
    #     current_user.about_me = form.bio.data
    #     db.session.commit()
    #     flash('Your changes have been saved.')
    #     return redirect(url_for('main.update'))
    
    # elif request.method == 'GET':
    #     form.name.data = current_user.name
    #     form.bio.data = current_user.bio
   

    #     return redirect(url_for('main.profile'))
    # return render_template('update.html',form=form)


@main.route('/user/<name>', methods=['GET','POST'])
@login_required
def profile(name):
    form = UpdateForm()
   
    return render_template('profile.html',title='profile',form=form)