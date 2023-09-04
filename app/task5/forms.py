from flask_security.forms import ChangePasswordForm
from wtforms import PasswordField

class CustomChangePasswordForm(ChangePasswordForm):
    new_password = PasswordField('New Password')








    



    
