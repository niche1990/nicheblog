from flask import render_template, url_for
from . import blue

@blue.route('/about')
def about():
    return render_template('about.html')
