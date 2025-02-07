from flask  import Flask

def create_app():
    #initialising the app
    app = Flask(__name__)
    #For handling cookies and cache
    app.config['SECRET_KEY'] = 'hfjauskyfed kwjgadjfgsh'

    #Importing BLUEPRINTS. we are importing the URL's and roots from views and auth
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app