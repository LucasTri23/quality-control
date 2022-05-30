from datetime import timedelta

from instance import config


class BaseConfig():
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{config.local_user}:{config.local_password}@{config.local_host}/{config.local_db}'
    DATABASE_CONNECT_OPTIONS = {}
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)
    JWT_ALGORITHM = 'HS512'
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
    JWT_TOKEN_LOCATION = ['headers']
    JWT_COOKIE_CSRF_PROTECT = False
    JWT_COOKIE_SECURE = True

class ProductionConfig(BaseConfig):
    # Production Configurations
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{config.remote_user}:{config.remote_password}@{config.remote_host}/{config.remote_db}'
    JWT_ALGORITHM = "HS512"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(seconds=600)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(seconds=604800)
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
    JWT_TOKEN_LOCATION = ['headers']
    JWT_COOKIE_CSRF_PROTECT = False

