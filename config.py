from instance import config
#Enable dev enviroment
DEBUG = True

SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{config.user}:{config.password}@{config.host}/{config.db}'

DATABASE_CONNECT_OPTIONS = {}

SQLALCHEMY_TRACK_MODIFICATIONS = False
