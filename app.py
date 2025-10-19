from flask import Flask
from extensions import db, bcrypt, login_manager
from routes import routes
from models import User, Farmer

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key-here'  # Replace with a secure key
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///farmers.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'routes.login'

    # Register blueprint
    app.register_blueprint(routes)

    # Initialize DB tables
    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)