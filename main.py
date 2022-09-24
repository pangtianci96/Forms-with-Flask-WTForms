from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap
import os


class MyForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(), Email()])
    password = PasswordField(label='password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Login')


app = Flask(__name__)
Bootstrap(app)

form_key = os.urandom(12)
# print(form_key)
app.secret_key = form_key

admin_email = os.environ['ADMIN_EMAIL']
admin_password = os.environ['ADMIN_PASSWORD']


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = MyForm()
    if login_form.validate_on_submit():
        if login_form.email.data == admin_email and login_form.password.data == admin_password:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
