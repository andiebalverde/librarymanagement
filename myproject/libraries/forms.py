from flask_wtf import Form
from wtforms import StringField, IntegerField, SubmitField

class AddForm(Form):

    library_id = IntegerField("Id of Library: ")
    name = StringField('Name of Library:')
    city = StringField('City of Library:')
    state = StringField('State:')
    postal_code = StringField('Postal Code:')
    submit = SubmitField('Add Library')

class DelForm(Form):

    id = IntegerField('Id Number of Library to Remove:')
    submit = SubmitField('Remove Library')
