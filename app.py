# This is app.py, this is the main file called.
from myproject import app
from flask import render_template, request
from myproject import db


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/tx', methods=['GET'])
def dropdown():
    #colours = ['Red', 'Blue', 'Black', 'Orange']
    colours = [r.email for r in db.session.query('books').filter_by(name=name).distinct()]
    return render_template('tx.html', colours=colours)

if __name__ == '__main__':
    app.run(debug=True)

