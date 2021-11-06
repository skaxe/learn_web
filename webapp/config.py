import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))

WEATHER_DEFAULT_CITY = 'Moscow,Russia'
WEATHER_API_KEY = '5f2afdbcfb404e97b5c114738212509'
WEATHER_URL = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')
SECRET_KEY = "ASFAJGKJDS124332jhj$jhjfdahsa@#@1asddxz"
REMEMBER_COOKIE_DURATION = timedelta(days=5)#запоминание логина на 5 дней
EXEMPT_METHODS = set(['OPTIONS'])