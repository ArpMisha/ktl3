from wtforms import Form, SelectField, StringField
from wtforms.validators import IPAddress, DataRequired

#ИС
class IsForm(Form):
    kr_name = StringField('kr_name', validators=[DataRequired()]) # краткое имя
    name = StringField('name', [DataRequired()]) # полное имя
    kategor = StringField('kategor', [DataRequired()])
    tip = StringField('tip', [DataRequired()])
    








    



    
