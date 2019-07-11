from flask import render_template, request, redirect, url_for
from . import main
from ..models import User, Subscription
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
        subscribe(email=form.email.data)

    return render_template('index.html', SubscriptionForm=form)


@main.route('/subscribe/<email>')
def subscribe_handler(email):
    subscribe(email)
    return redirect(url_for('main.index'))


def subscribe(email):
    new_subscription = Subscription(email=email)
    new_subscription.save_email()

    send_welcome_email(email=email)


@main.route('/unsubscribe/<email>')
def unsubscribe_handler(email):
    unsubscribe(email)
    return redirect(url_for('main.index'))


def unsubscribe(email):
    sub = Subscription.query.filter_by(email=email).first()
    if sub is not None:
        db.session.delete(sub)
        db.session.commit()

    mail_message("Farewell from Fa-Shoni", "email/unsubscribe_user", email, email=email)


def send_welcome_email(email):
    '''
    Send welcome email to new subscriber
    '''
    mail_message("Welcome to Fa-Shoni", "email/welcome_user", email, email=email)


@main.route('/designers')
def designer():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'This is designers page'
    return render_template('designers.html', title='title')
