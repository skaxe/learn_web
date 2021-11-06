
#Создание пользователя
from getpass import getpass#Похоже на инпут, но не печатает, то что вводит пользователь звездочками заполняет
import sys #модуль взаимодействия с системыми функциями(шоб ретерн не делать)

from webapp import create_app
from webapp.db import db 
from webapp.news.models import User

app = create_app()

with app.app_context(): # запрашивает имя пользователя
    username = input('Введите имя пользователя: ')

    if User.query.filter(User.username == username).count():# проверка на существование пользователя
        print('Такой пользователь уже есть')#Достает это все из БД и сверяет (query)
        sys.exit(0) # если пользователь есть -> выход из прогграммы

    password1 = getpass('введите пароль')
    password2 = getpass('введите пароль')
    if not password1 == password2:# проверка пароля
        print('Пароли не одинаковые')
        sys.exit(0)

    new_user = User(username=username, role='admin') #создание юзера
    new_user.set_password(password1)# установление пароля

    db.session.add(new_user)# добавление пользователя в БД
    db.session.commit()#подтверждаем
    print('User with id {} added'.format(new_user.id))#Печатаем, что создан пользователь