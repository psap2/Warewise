from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    supplier_id = db.Column(db.Integer, db.ForeignKey('suppliers.id'), nullable=False)

    def restock(self, amount):
        """Increment the quantity of product stock."""
        self.quantity += amount
        db.session.commit()

    def update_price(self, new_price):
        """Update the price of the product."""
        self.price = new_price
        db.session.commit()

class Supplier(db.Model):
    __tablename__ = 'suppliers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact_info = db.Column(db.String(200)) 
    products = db.relationship('Product', backref='supplier', lazy='dynamic')

    def add_product(self, product_name, quantity, price):
        """Add a new product to the supplier."""
        new_product = Product(name=product_name, quantity=quantity, price=price, supplier_id=self.id)
        db.session.add(new_product)
        db.session.commit()

#database for users
class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)


def init_app(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
