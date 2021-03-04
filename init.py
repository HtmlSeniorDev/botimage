from flask import Flask
from SERVER_CONFIG import MONGO_ADDRESS, MONGO_PORT

app = Flask(__name__)


def create_app():
    app.config["MONGO_URI"] = "mongodb://" + MONGO_ADDRESS + ":" + str(MONGO_PORT) + "/chat"
    app.config['SECRET_KEY'] = 'secret!'

    from db import mongo


    mongo.init_app(app)

    return app
