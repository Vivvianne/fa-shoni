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
        try:
            new_subscription = Subscription(email=form.email.data)
            new_subscription.save_email()

            send_welcome_email(email=form.email.data)
        except:
            print("Database Exception", flush = True)

    return render_template('index.html', SubscriptionForm = form)

def send_welcome_email(email):
    '''
    Send welcome email to new subscriber
    '''
    mail_message("Welcome to Fa-Shoni","email/welcome_user", email)
    
@main.route('/children')
def children():
    return render_template('children.html')
@main.route('/men')
def men():
    return render_template('men.html')
@main.route('/women')
def women():
    return render_template('women.html')

