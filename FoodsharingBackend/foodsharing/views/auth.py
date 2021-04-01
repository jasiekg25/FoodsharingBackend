from flask import Blueprint, render_template, flash, redirect
from flask.helpers import url_for
from foodsharing.forms import RegistartionForm, LoginForm


auth = Blueprint('auth', __name__)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistartionForm()
    if form.validate_on_submit():
        flash('Account created!')
        return redirect(url_for('home.home_page'))
    return render_template('register.html', title='Register', form=form)


@auth.route('/login')
def login():
    # TODO
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)