from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, DateField
from wtforms.validators import DataRequired
from ..models import User,Subscription



class SubscriptionForm(FlaskForm):
    email = StringField('Insert your email here', validators=[DataRequired()])
    subscribe = SubmitField()