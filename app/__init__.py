from flask import Flask
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.ProductionConfig')
app.config['JSON_AS_ASCII'] = False
app.config['SECRET_KEY'] = 'secret'
db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()


def create_app():
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)

    # import models
    from app.models import device
    from app.models import user
    from app.models import employee

    # implement logic to see if the bank already exists
    with app.app_context():
        db.create_all()
    # #import controllers
    from app.controllers.device_controller import DeviceController
    from app.controllers.user_controller import UserController
    from app.controllers.test_controller import TestController
    from app.controllers.result_controller import ResultController
    from app.controllers.auth_controller import AuthController

    app.register_blueprint(DeviceController.device_controller, url_prefix="/api/v1")
    app.register_blueprint(UserController.user_controller, url_prefix="/api/v1")
    app.register_blueprint(TestController.test_controller, url_prefix="/api/v1")
    app.register_blueprint(ResultController.result_controller, url_prefix="/api/v1")
    app.register_blueprint(AuthController.auth_controller, url_prefix="/api/v1")

    return app
