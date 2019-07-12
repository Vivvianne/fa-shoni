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
        subscribe(email=form.email.data)

    return render_template('index.html', SubscriptionForm=form)


@main.route('/subscribe/<email>')
def subscribe_handler(email):
    subscribe(email)
    return redirect(url_for('main.index'))


def subscribe(email):
    try:
        new_subscription = Subscription(email=email)
        new_subscription.save_email()

        send_welcome_email(email=email)
    except Exception as e:
        print("Error while subscribing email:" + str(e), flush=True)


@main.route('/unsubscribe/<email>')
def unsubscribe_handler(email):
    unsubscribe(email)
    return redirect(url_for('main.index'))


def unsubscribe(email):

    try:
        sub = Subscription.query.filter_by(email=email).first()
        if sub is not None:
            db.session.delete(sub)
            db.session.commit()

        mail_message("Farewell from Fa-Shoni", "email/unsubscribe_user", email, email=email)
    except Exception as e:
        print("Error while unsubscribing email:" + str(e), flush=True)


def send_welcome_email(email):
    '''
    Send welcome email to new subscriber
    '''
    mail_message("Welcome to Fa-Shoni", "email/welcome_user", email, email=email)
    
@main.route('/children')
def children():
    return render_template('children.html')
@main.route('/men')
def men():
    return render_template('men.html')
@main.route('/women')
def women():
    return render_template('women.html')
@main.route('/designers')
def designer():

   '''
   View root page function that returns the index page and its data
   '''
   title='This is designers page'
   return render_template('designers.html',title='title')

@main.route('/designers',methods=['GET'])
def designers():
    
    return render_template('designers.html')
@main.route('/designers')
def search_designers(search):
    designers = []
    search_string = search.data['search']
    if search_string:
        if search.data['select'] == 'Artist':
            qry = db_session.query(User, Profile).filter(
                Profile.id==User.profile_id).filter(
                    Profile.name.contains(search_string))
            results = [item[0] for item in qry.all()]
        elif search.data['select'] == 'User':
            qry = db_session.query(User).filter(
                User.title.contains(search_string))
            results = qry.all()
    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        table = Profile(profile)
        table.border = True
        return render_template('designer.html', table=table)
    

@main.route('/user/<name>', methods=['GET','POST'])
@login_required
def profile(name):
    form = UpdateForm()
   
    return render_template('profile.html',title='profile',form=form)

@main.route('/user/<name>/update/pic',methods= ['POST'])
@login_required
def update_pic(name):
    user = User.query.filter_by(username = name).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',name=name))








