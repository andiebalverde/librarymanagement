from flask_wtf import Form
from wtforms import StringField, IntegerField, SubmitField

class AddForm(Form):

    library_activity_id = IntegerField("Id of Library Activity: ")
    #activity_type = StringField('Activity Type:')
    user_id = StringField('User ID:')
    library_book_id = StringField('Library Book ID:')
    checked_out_at = StringField('Checked Out At:')
    checked_in_at = SubmitField('Checked In At:')
    submit = SubmitField('Add Library Activity')

class DelForm(Form):

    id = IntegerField('Id Number of Library to Remove:')
    submit = SubmitField('Remove Library')
