from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, DateField
from wtforms.validators import DataRequired
from ..models import User,Subscription



class SubscriptionForm(FlaskForm):
    email = StringField('', validators=[DataRequired()])
    subscribe = SubmitField()