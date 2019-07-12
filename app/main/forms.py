from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, DateField,PasswordField
from wtforms.validators import DataRequired,Length
from wtforms.validators import Required,EqualTo
from ..models import User,Subscription



class SubscriptionForm(FlaskForm):
    email = StringField('', validators=[DataRequired()])
    subscribe = SubmitField()
    
class UpdateForm(FlaskForm):
       
    name = StringField('Your name',validators=[Required()])
    location = StringField('Country/City',validators=[Required()])
    contact =StringField('Email/phone',validators=[Required()])
    bio = TextAreaField('Add a description',validators=[Length(min=0, max=140)])
    submit = SubmitField('submit')