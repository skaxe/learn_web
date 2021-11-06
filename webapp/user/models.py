from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from webapp.db import db

class User(db.Model, UserMixin): #Заполняет поля для БД для юзера пароль UserMixin определяет актив 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, unique=True)
    password = db.Column(db.String(128))
    role = db.Column(db.String(10), index=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)#Зашифровывает пароль функцией

    def check_password(self, password):# Принимает зашифрованый пароль из БД и строку переданную пользователем
        return check_password_hash(self.password, password)#Нужно вернуть тру или фаллс чтобы понят ьверный пароль или нет

    @property    
    def is_admin(self): #проверка на админа 
        return self.role == 'admin'

    def __repr__(self):
        return '<User name = {} id ={}'.format(self.username, self.id)