from datetime import datetime, timezone
from flask import flash, render_template, session, redirect, url_for, current_app
from .. import db
from ..models import User
from ..email import send_email
from . import main
from .forms import NameForm


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()

        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            flash('Looks like you are a new user!')
            session['known'] = False
            print('dziala1')
            if current_app.config['FLASKY_ADMIN']:
                print('dziala2')
                send_email(current_app.config['FLASKY_ADMIN'], 'New User',
                           'mail/new_user', user=user)
        else:
            session['known'] = True

        old_name = session.get('name')
        session['name'] = form.name.data

        if old_name is not None and old_name != session['name']:
            flash('Looks like you have changed your name!')

        return redirect(url_for('.index'))
    
    return render_template('index.html', current_time=datetime.now(timezone.utc),
                            form=form, name=session.get('name'), 
                            known=session.get('known', False))

@main.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)