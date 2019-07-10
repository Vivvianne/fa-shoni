from flask import render_template,request,redirect,url_for
from . import main
from ..models import User,Subscription
from .. import db
from .forms import SubscriptionForm
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