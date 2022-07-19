from wtforms.form import Form
from wtforms.fields import StringField, IntegerField
from wtforms.validators import  Optional, Email, DataRequired

class ProfileValidator(Form):
    name = StringField('name', validators=[DataRequired()])
    email  = StringField('email', validators=[Optional(), Email()])
    age = IntegerField('age', validators=[Optional()])
