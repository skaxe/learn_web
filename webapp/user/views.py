from flask import Blueprint, render_template, flash, redirect, url_for #flash - позволяет передавать сообщения между route-ами rederict- делает перенаправление со страницы на страницу url; - позволяет получить юрл 
from flask_login import current_user, login_user, logout_user #менеджер логина? кароче дял работы с логином

from webapp.user.forms import LoginForm
from webapp.user.models import User

blueprint = Blueprint('user', __name__, url_prefix='/users')

@blueprint.route('/login')
def login():#функция авторизации
    if current_user.is_authenticated:#Проверка на аутотифенкацию ( чтобы при обновлении юзер не пропадал)
        return redirect(url_for('news.index'))
    title = "Авторизация"
    login_form = LoginForm()# из webapp.forms экземпляр формы
    return render_template('user/login.html', page_title=title, form=login_form)# так же передача в login.html

@blueprint.route('/process-login', methods=['POST'])#какие методы обрабатывает роут(т.к. мы хотим обработать POST) /process-login'
def process_login():
    form = LoginForm()#экземпляр формы
    if form.validate_on_submit(): #форма валидируется ( проверяте на ошибки ( заполнены ли поля и тд))
        user = User.query.filter_by(username=form.username.data).first()#запрашиваем из бд данные юзернейма ИЗ БД БЕРЕТСЯ ПЕРЕМЕННАЯ
        if user and user.check_password(form.password.data): #проверка на существование пользователя и проверка пароля                
            login_user(user, remember=form.remember_me.data)#запоминание пользователя
            login_user(user)#заолгинили пользователя
            flash('Вы вошли на сайт')
            return redirect(url_for('news.index'))#перекидываем на странциу индекс

    flash('Неправильное имя пользователя или пароль')#если не прошло
    return redirect(url_for('user.login')) #возвращаем на страницу логина  
@blueprint.route('/logout')#возможность выйти из пользователя
def logout():
    logout_user()#разлогинивание
    flash('вы успешно разлогинились')#алерт через флэш в хтмл
    return redirect(url_for('news.index')) #перенаправление на другую страницу
