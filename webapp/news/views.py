from flask import Blueprint, current_app, render_template

from webapp.news.models import News
from webapp.weather import weather_city

blueprint = Blueprint('news', __name__)


@blueprint.route('/')
def index():#Функция для отображения новостей
    title = 'Новости Python'#заголовок
    weather = weather_city(current_app.config['WEATHER_DEFAULT_CITY'])# опредение погоды в выбранном городе из config
    news_list = News.query.order_by(News.published.desc()).all()#доставание query из БД списка новостей
    return render_template('news/index.html', page_title = title, weather = weather, news_list = news_list) # передача в index.html нужных параметров