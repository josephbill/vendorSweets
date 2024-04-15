from models.dbmodel import db, Sweet, Vendor, VendorSweet
from flask_migrate import Migrate
from flask import Flask, request, make_response, current_app
from flask_restful import Api, Resource
from flask_cors import CORS

def create_app():
    # create flask app
    app = Flask(__name__)
    CORS(app)

    # Get specific configs. That we did in DB and ability to track modifications configured in app.py
    app.config.from_object('config.Config')

    # initialize app with db
    db.init_app(app)
    api = Api(app)

    # Establish routes
    class Home(Resource):
        def get(self):
            return '<h1>Code challenge</h1>'
        
    api.add_resource(Home, '/')

    return app
