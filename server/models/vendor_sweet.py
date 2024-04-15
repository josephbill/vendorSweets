from models.dbmodel import db, SerializerMixin, validates, association_proxy

class VendorSweet(db.Model, SerializerMixin):
    __tablename__ = 'vendor_sweets'

    __table_args__ = (
        db.UniqueConstraint('vendor_id', 'sweet_id'),
        db.CheckConstraint('price >=0', name='Price should be > 0')
    )

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)

    # Add relationships
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.id'))
    sweet_id = db.Column(db.Integer, db.ForeignKey('sweets.id'))
    # Add serialization
    
    # Add validation
    @validates('price')
    def validate_price(self, key, price):
        if price is None:
            raise ValueError("Invalid price")
        if price >= 0:
            return price
        else:
            raise ValueError("Invalid price")

    
    def __repr__(self):
        return f'<VendorSweet {self.id}>'
