from instance import config
#Enable dev enviroment
DEBUG = True

SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{config.local_user}:{config.local_password}@{config.local_host}/{config.local_db}'

DATABASE_CONNECT_OPTIONS = {}

SQLALCHEMY_TRACK_MODIFICATIONS = False
