from flask import Flaskfrom flask import Flask

from extensions import db, bcrypt, login_managerfrom extensions import db, bcrypt, login_manager

from routes import routesfrom routes import routes

from models import User, Farmerfrom models import User, Farmer



def create_app():def create_app():

    app = Flask(__name__)    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'your-secret-key-here'  # Replace with a secure key    app.config['SECRET_KEY'] = 'your-secret-key-here'  # Replace with a secure key

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///farmers.db'    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///farmers.db'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



    # Initialize extensions    # Initialize extensions

    db.init_app(app)    db.init_app(app)

    bcrypt.init_app(app)    bcrypt.init_app(app)

    login_manager.init_app(app)    login_manager.init_app(app)

    login_manager.login_view = 'routes.login'    login_manager.login_view = 'routes.login'



    # Register blueprint    # Register blueprint

    app.register_blueprint(routes)    app.register_blueprint(routes)



    # Initialize DB tables    # Initialize DB tables

    with app.app_context():    with app.app_context():

        db.create_all()        db.create_all()



    return app    return app



# Create app instance for Gunicornif __name__ == '__main__':

app = create_app()    app = create_app()

    app.run(debug=True)
if __name__ == '__main__':
    app.run(debug=True)
