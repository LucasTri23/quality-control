from instance import config
#Enable dev enviroment
DEBUG = True

SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{config.remote_user}:{config.remote_password}@{config.remote_host}/{config.remote_db}'

DATABASE_CONNECT_OPTIONS = {}

SQLALCHEMY_TRACK_MODIFICATIONS = False
