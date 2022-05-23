from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app)

#import models
from app.models import device
from app.models import user
from app.models import employee
db.create_all()
# #import controllers
from app.controllers.device_controller import DeviceController
from app.controllers.user_controller import UserController

app.register_blueprint(DeviceController.device_controller, url_prefix="/api/v1")
app.register_blueprint(UserController.user_controller, url_prefix="/api/v1")

