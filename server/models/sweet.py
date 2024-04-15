from models.dbmodel import db, SerializerMixin, validates, association_proxy
from models.vendor_sweet import VendorSweet

class Sweet(db.Model, SerializerMixin):
    __tablename__ = 'sweets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    # Add relationship
    vendor_sweets = db.relationship('VendorSweet', backref='sweet', cascade='all, delete-orphan')
    vendors = association_proxy('vendor_sweets', 'vendor', creator=lambda vendor_obj : VendorSweet(vendor = vendor_obj))
    
    # Add serialization
    serialize_rules = ('-vendor_sweets.sweet', '-vendor_sweets.vendor')
    
    def __repr__(self):
        return f'<Sweet {self.id}>'
