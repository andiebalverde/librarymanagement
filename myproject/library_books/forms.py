from flask_wtf import Form
from wtforms import StringField, IntegerField, SubmitField

class AddForm(Form):
    library_id = StringField('Library ID:')
    submit = SubmitField('Add Library Book')
