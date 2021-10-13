from flask_wtf import Form
from wtforms import StringField, IntegerField, SubmitField

class AddForm(Form):

    title = StringField('Title:')
    author_name = StringField('Author:')
    isdn_num = StringField('ISDN:')
    genre = StringField('Genre:')
    description = StringField('Description:')
    submit = SubmitField('Add Book')

class DelForm(Form):

    id = IntegerField('Id Number of Puppy to Remove:')
    submit = SubmitField('Remove Puppy')
