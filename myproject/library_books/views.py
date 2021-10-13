from flask import Blueprint,render_template,redirect,url_for, request
from myproject import db
from myproject.models import LibraryBooks, Libraries, Books, LibraryActivities
from myproject.library_books.forms import AddForm

librarybooks_blueprint = Blueprint('library_books',
                              __name__,
                              template_folder='templates/library_books')

@librarybooks_blueprint.route('/add', methods=['GET', 'POST'])
def add():

    form = AddForm()
    libraries = list(Libraries.query.all())  # query all libraries
    books = list(Books.query.all())

    if form.validate_on_submit():
        #library_id = form.library_id.data
        library_id = request.form.get('library')
        #book_id = form.book_id.data
        book_id = request.form.get('book')
        # Add new library_book to database
        new_library_book = LibraryBooks(library_id=library_id, book_id=book_id, last_library_activity_id="Created")
        db.session.add(new_library_book)
        print(f"This is the new library book: {new_library_book}")
        db.session.flush()
        db.session.commit()
        library_books = LibraryBooks.query.all()

        new_library_activity = LibraryActivities(activity_type=new_library_book.last_library_activity_id, user_id=None, library_book_id=new_library_book.library_book_id, checked_out_at=None, checked_in_at=None)
        db.session.add(new_library_activity)
        print(f"This is the new library activity: {new_library_activity}")
        db.session.flush()
        db.session.commit()

        #return redirect(url_for('library_books.list'))
        return render_template('list_library_book.html', library_books=library_books)
    return render_template('add_library_book.html', form=form, books=books, libraries=libraries)

#@librarybooks_blueprint.route('/list')
#def list(self):
#    library_books = LibraryBooks.query.all()
#    return render_template('list_library_book.html', library_books=library_books)
