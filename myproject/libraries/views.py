from flask import Blueprint,render_template,redirect,url_for
from myproject import db
from myproject.libraries.forms import AddForm, DelForm
from myproject.models import Libraries

libraries_blueprint = Blueprint('libraries',
                              __name__,
                              template_folder='templates/libraries')

@libraries_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()

    if form.validate_on_submit():
        library_id = form.library_id.data
        name = form.name.data
        city = form.city.data
        state = form.state.data
        postal_code = form.postal_code.data

        # Add new Library to database
        new_library = Libraries(name=name, city=city, state=state, postal_code=postal_code)
        db.session.add(new_library)
        db.session.commit()

        return redirect(url_for('libraries.list_libraries'))

    return render_template('addlib.html',form=form)

@libraries_blueprint.route('/list_libraries')
def list_libraries():
    # Grab list of Libraries from database.
    libraries = Libraries.query.all()
    return render_template('list_libraries.html', libraries=libraries)

@libraries_blueprint.route('/delete', methods=['GET', 'POST'])
def delete():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        lib = Libraries.query.get(id)
        db.session.delete(lib)
        db.session.commit()

        return redirect(url_for('libraries.list'))
    return render_template('delete.html',form=form)
