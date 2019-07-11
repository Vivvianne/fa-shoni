from flask import render_template,request,redirect,url_for
from . import main
from ..models import User,Subscription, Profile
from .. import db
from .forms import SubscriptionForm,UpdateForm
from ..email import mail_message




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

@main.route('/update', methods=['GET', 'POST'])
def update():

    form = UpdateForm()
    
    if form.validate_on_submit():
        user = Profile(name =form.name.data, contact= form.contact.data, bio = form.bio.data, adress = form.location.data)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('main.profile'))
    return render_template('update.html',form=form)


@main.route('/profile<int:id>', methods=['GET','POST'])
@login_req
def profile():
    profile = profile.get_profile(id)
    return render_template('profile.html',profile=profile)