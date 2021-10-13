from flask import Blueprint,render_template,redirect,url_for, request
from myproject import db
from myproject.models import LibraryBooks, Libraries, Books, Users, LibraryActivities, ActTypeEnum
from myproject.library_activities.forms import AddForm

libraryactivities_blueprint = Blueprint('library_activities',
                              __name__,
                              template_folder='templates/library_activities')


@libraryactivities_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()
    users = list(Users.query.all())
    act_type_enum = [(a.value, a.name) for a in ActTypeEnum]
    library_book_ids = list(LibraryBooks.query.all())

    if form.validate_on_submit():
        activity_type = str(request.form.get('act_type'))
        type = list(activity_type.split(","))
        user_id = list(request.form.get('user'))
        #comp_select = request.form.get('comp_select')

        print(f"activity type is: {str(activity_type)}")  # just to see what select is

        library_book_id = request.form.get('library_book_id')
        if form.checked_out_at.data:
            checked_out_at = form.checked_out_at.data
        else:
            checked_out_at = None
        #if form.checked_in_at.data:
            #checked_in_at = form.checked_in_at.data
        #else:
        #    checked_in_at = None
        checked_in_at = (request.form.get('checked_in_at.value'))
        print(f"checked in at: {str(checked_in_at)}")  # just to see what select is
        # Add new Library Activity to database
        new_library_activity = LibraryActivities(activity_type=type[-1], user_id=int(user_id[-1]), library_book_id=library_book_id, checked_out_at=checked_out_at, checked_in_at=checked_in_at)
        db.session.add(new_library_activity)
        print(f"This is the new library book: {new_library_activity}")
        db.session.flush()
        db.session.commit()
        library_activities = LibraryActivities.query.all()


        lbid = new_library_activity.library_book_id[-1]
        laid = new_library_activity.library_activity_id
        print(f"lbid is: {lbid} and library_activity_id is {laid}")
        #db.session.execute("UPDATE library_books SET last_library_activity_id = ? WHERE library_book_id = ?", lbid, laid)
        admin = LibraryBooks.query.filter_by(library_book_id=lbid).first()
        #LibraryBooks.query.filter_by(library_book_id=lbid).first()
        admin.last_library_activity_id = laid
        db.session.commit()

        print(f"admin.last_library_activity_id is {admin.last_library_activity_id}")

        #return redirect(url_for('library_books.list'))
        return render_template('list_library_activities.html', library_activities=library_activities)
    return render_template('add_library_activity.html', form=form, act_type_enum=act_type_enum, users=users, library_book_ids=library_book_ids)
