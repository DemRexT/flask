from flask import Flask, request, render_template, flash
from module import db, User
from form import RegistrationForm
from flask_wtf.csrf import CSRFProtect
from sqlalchemy.exc import IntegrityError
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SECRET_KEY'] = b'6a8d5fde5f4075126c6b23a4f42b41ab100426cf9c4a9c2a0a5b91dc5dc57e2b'
db.init_app(app)
csrf = CSRFProtect(app)
bcrypt = Bcrypt(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')



@app.route('/')
def lider():
    return render_template('base.html')


@app.route('/regi/', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        name = form.username.data
        lastname = form.last_name.data
        email = form.email.data
        password = form.password.data
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(username = name, lastname = lastname, email = email, password = hashed_password)
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            flash('Пользователь с данным Email уже существует', 'error')
            return render_template('registration.html', form=form)
    return render_template('registration.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)

