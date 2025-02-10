from flask  import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

#creating an instance of the database
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    #initialising the app
    app = Flask(__name__)
    #For handling cookies and cache
    app.config['SECRET_KEY'] = 'hfjauskyfed kwjgadjfgsh'
    #Letting the flask know about the database location
    app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{DB_NAME}'
    #Initialising the database
    db.init_app(app)

    #Importing BLUEPRINTS. we are importing the URL's and roots from views and auth
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    
    from .models import User, Note
    create_database(app)

    login_manager=LoginManager()
    login_manager.login_view='auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
#check if database is created or not 
def create_database(app):
    if not path.exists('website/'+DB_NAME):
        with app.app_context():  # Use app context
            db.create_all()
        print('Created Database!')

