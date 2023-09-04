from wtforms import Form, SelectField, StringField
from wtforms.validators import IPAddress, DataRequired


class UserForm(Form):
    email = StringField('email', validators=[DataRequired()]) 
    password = StringField('password', [DataRequired()]) 
