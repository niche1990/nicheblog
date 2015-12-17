from flask import redirect, url_for, render_template
from . import blue

@blue.route('/')
def index():
    return redirect(url_for('home.home'))

@blue.route('/home')
def home():
    return render_template('home.html')
