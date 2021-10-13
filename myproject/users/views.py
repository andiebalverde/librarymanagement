from flask import Blueprint,render_template,redirect,url_for, request
from myproject import db
from myproject.users.forms import AddForm,DelForm, ListForm, ListLibForm
from myproject.models import Users, Libraries

users_blueprint = Blueprint('users',
                              __name__,
                              template_folder='templates/users')

@users_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data

        # Add new User to database
        new_user = Users(name)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('users.list'))

    return render_template('addlib.html',form=form)

@users_blueprint.route('/list')
def list():
    users = Users.query.all()
    return render_template('list_users.html', users=users)



@users_blueprint.route('/list_by_act', methods=['GET', 'POST'])
def list_by_act():
    form = ListForm()
    users = Users.query.all()

    if form.validate_on_submit():
        #user_id = form.user_id.data
        user_id = request.form.get('user')
        db.session.query()
        #users = db.session.execute("SELECT * from library_activities WHERE user_id = %s", {user_id})
        user_selected1 = db.session.execute("SELECT * from library_activities WHERE user_id = :ui AND activity_type like '%checkout%'", {'ui': user_id})
        user_selected = [dict(row) for row in user_selected1]
        print(f"user id is {user_id} and user_selected is {user_selected}")

        return render_template('list_users_activities.html', form=form, users=users, user_selected=user_selected)
    return render_template('list_users_activities.html', form=form, users=users)

@users_blueprint.route('/list_lib_checkout', methods=['GET', 'POST'])
def list_lib_checkout():
    form = ListLibForm()
    libraries = Libraries.query.all()

    if form.validate_on_submit():
        #user_id = form.user_id.data
        library1 = request.form.get('library')
        library = int(library1[-1])
        db.session.query()

        #lib_selected1 = db.session.execute(
        #    "SELECT * FROM library_activities JOIN library_books ON library_activities.library_book_id = library_books.library_book_id "
        #                                    "JOIN libraries WHERE libraries.library_id = 'lid' AND library_activities.activity_type like '%checkout%'", {'lid': library})
        lib_selected1 = db.session.execute("SELECT * from library_activities WHERE activity_type like '%checkout%'")

        lib_selected = [dict(row) for row in lib_selected1]
        print(f"Library is {library} and lib_selected is {lib_selected} and lib_selected1 is {lib_selected1}")

        return render_template('list_library_checkouts.html', form=form, libraries=libraries, user_selected=lib_selected)
    return render_template('list_library_checkouts.html', form=form, libraries=libraries)


@users_blueprint.route('/delete', methods=['GET', 'POST'])
def delete():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        user = Users.query.get(id)
        db.session.delete(user)
        db.session.commit()

        return redirect(url_for('users.list'))
    return render_template('delete.html',form=form)
