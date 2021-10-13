from flask_wtf import Form
from wtforms import StringField, IntegerField, SubmitField

class AddForm(Form):

    submit = SubmitField('Add Library Book')
