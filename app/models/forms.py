from flask_wtf import Form, FlaskForm
from wtforms import StringField, BooleanField, PasswordField, validators
from wtforms.validators import DataRequired, InputRequired, Length

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(max=29)])
    email = StringField(validators=[InputRequired(), Length(max=29)])
    passwd = PasswordField(validators=[Length(min=4, max=16)])
    
class uploadForm(Form):
    pass