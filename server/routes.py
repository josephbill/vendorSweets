from models.dbmodel import db, Sweet, Vendor, VendorSweet
from flask_migrate import Migrate
from flask import Flask, request, make_response, current_app, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
from sqlalchemy.exc import IntegrityError

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

    class Vendors(Resource):
        def get(self):
            vendors = [vendor.to_dict(rules=('-vendor_sweets',)) for vendor in Vendor.query.all()]
            response = make_response(jsonify(vendors), 200)
            return response
    
    api.add_resource(Vendors, '/vendors')

    class VendorById(Resource):
        def get(self, id):
            vendor = Vendor.query.filter(Vendor.id == id).first()
            if vendor:
                response = make_response(jsonify(vendor.to_dict()), 200)
            else:
                response = make_response(jsonify({"error": "Vendor not found"}), 404)
            return response

    api.add_resource(VendorById, '/vendors/<int:id>')

    class Sweets(Resource):
        def get(self):
            sweets = [sweet.to_dict(rules=('-vendor_sweets',)) for sweet in Sweet.query.all()]
            response = make_response(jsonify(sweets), 200)
            return response
        
    api.add_resource(Sweets, '/sweets')

    class SweetById(Resource):
        def get(self, id):
            sweet = Sweet.query.filter(Sweet.id == id).first()
            if sweet:
                response = make_response(jsonify(sweet.to_dict(rules=('-vendor_sweets',))), 200)
            else:
                response = make_response(jsonify({"error": "Sweet not found"}), 404)
            return response

    api.add_resource(SweetById, '/sweets/<int:id>')

    class VendorSweets(Resource):
        def post(self):
            data = request.get_json()
            vendor_sweet = VendorSweet(
                price = data.get('price'),
                vendor_id = data.get('vendor_id'),
                sweet_id = data.get('sweet_id')
            )
            try:
                db.session.add(vendor_sweet)
                db.session.commit()
                response = make_response(jsonify(vendor_sweet.to_dict()), 201)
            except ValueError as e:
                db.session.rollback()
                response = make_response(jsonify({"errors" : ["validation errors"]}), 400)
            return response

    api.add_resource(VendorSweets, '/vendor_sweets')

    class VendorSweetsById(Resource):
        def delete(self, id):
            vendor_sweet = VendorSweet.query.filter(VendorSweet.id == id).first()
            if vendor_sweet:
                db.session.delete(vendor_sweet)
                db.session.commit()
                response = make_response({}, 204)
            else:
                response = make_response({"error": "VendorSweet not found"}, 404)

            return response

    api.add_resource(VendorSweetsById, '/vendor_sweets/<int:id>')

    return app
