from flask_wtf import Form
from wtforms import StringField, IntegerField, SubmitField

class AddForm(Form):

    name = StringField('Name of User:')
    submit = SubmitField('Add User')

class DelForm(Form):

    id = IntegerField('Id Number of User to Remove:')
    submit = SubmitField('Remove User')

class ListForm(Form):
    user_id = StringField('User ID:')
    submit = SubmitField('Select User')


class ListLibForm(Form):
    library = StringField('Library ID:')
    submit = SubmitField('Select Library')
