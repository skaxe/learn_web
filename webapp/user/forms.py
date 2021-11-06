from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField, HiddenField, SelectField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    team_list = ['Team1', 'Team2', 'Team3', 'Team4']
    username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
    remember_me = BooleanField('Запомнить меня', default=True, render_kw={"class": "form-check-input"})#галочка дял запоминания пользователя
    submit = SubmitField('Отправить', render_kw={"class":"btn btn-primary"})