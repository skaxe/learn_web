from flask import Flask, render_template#flash - позволяет передавать сообщения между route-ами rederict- делает перенаправление со страницы на страницу url; - позволяет получить юрл 
from flask_login import LoginManager, current_user, login_required #менеджер логина? кароче дял работы с логином



from webapp.db import db
from webapp.admin.views import blueprint as admin_blueprint
from webapp.user.views import blueprint as user_blueprint
from webapp.user.models import User
from webapp.news.views import blueprint as news_blueprint
from webapp.news.models import News


#ЗАПУСК сервера set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)#делаем инит?

    login_manager = LoginManager() #создаем экземпляр логи менеджера(почти как в model db = SQLalchemy)
    login_manager.init_app(app)#
    login_manager.login_view = 'user.login'# название функции login

    app.register_blueprint(user_blueprint)
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(news_blueprint)

    @login_manager.user_loader#при заходе на страницу будет делать запрос в бд по ИД
    def load_user(user_id):
        return User.query.get(user_id)# возвращает юзера по айди 
  
       
    return app