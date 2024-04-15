from models.dbmodel import db, SerializerMixin, validates, association_proxy
from models.vendor_sweet import VendorSweet

class Vendor(db.Model, SerializerMixin):
    __tablename__ = 'vendors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    # Add relationship
    vendor_sweets = db.relationship('VendorSweet', backref='vendor', cascade='all, delete-orphan')
    sweets = association_proxy('vendor_sweets', 'sweet', creator=lambda sweet_obj : VendorSweet(sweet = sweet_obj))
    
    # Add serialization
    serialize_rules = ('-vendor_sweets.sweet', '-vendor_sweets.vendor')
    
    def __repr__(self):
        return f'<Vendor {self.id}>'

