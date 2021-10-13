from flask import Blueprint,render_template,redirect,url_for
from myproject import db
from myproject.books.forms import AddForm,DelForm
from myproject.models import Books

books_blueprint = Blueprint('books',
                              __name__,
                              template_folder='templates/books')

@books_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()

    if form.validate_on_submit():
        title = form.title.data
        author_name = form.author_name.data
        isdn_num = form.isdn_num.data
        genre = form.genre.data
        description = form.description.data

        # Add new Book to database
        new_boo = Books(title=title, author_name=author_name, isdn_num=isdn_num, genre=genre, description=description)
        db.session.add(new_boo)
        db.session.commit()
        books = Books.query.all()
        #return redirect(url_for('books.list', books=books)
        return render_template('list_users.html', books=books)

    return render_template('add.html',form=form)

@books_blueprint.route('/list')
def list():
    # Grab a list of Books from database.
    books = Books.query.all()
    return render_template('list_users.html', books=books)

@books_blueprint.route('/delete', methods=['GET', 'POST'])
def delete():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        boo = Books.query.get(id)
        boo = Books.query.get(id)
        db.session.delete(boo)
        db.session.commit()

        return redirect(url_for('books.list'))
    return render_template('delete.html',form=form)
