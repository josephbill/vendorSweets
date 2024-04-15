from models.dbmodel import db, SerializerMixin, validates, association_proxy

class VendorSweet(db.Model, SerializerMixin):
    __tablename__ = 'vendor_sweets'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)

    # Add relationships
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.id'))
    sweet_id = db.Column(db.Integer, db.ForeignKey('sweets.id'))
    # Add serialization
    
    # Add validation
    
    def __repr__(self):
        return f'<VendorSweet {self.id}>'
