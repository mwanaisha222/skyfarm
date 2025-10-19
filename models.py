from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from extensions import db, bcrypt

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.email}>'

class Farmer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    district = db.Column(db.String(100), nullable=False)
    sub_county = db.Column(db.String(100), nullable=False)
    crop = db.Column(db.String(50), nullable=False)
    language = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('farmers', lazy=True))
    
    # Marketplace fields
    product_name = db.Column(db.String(100), nullable=True)
    product_description = db.Column(db.Text, nullable=True)
    product_price = db.Column(db.Float, nullable=True)
    product_image = db.Column(db.String(200), nullable=True)  # URL or filename
    phone_number = db.Column(db.String(20), nullable=True)

    def __repr__(self):
        return f'<Farmer {self.name}>'