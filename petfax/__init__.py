from flask import Flask
  
  
#config
def create_app():
    app = Flask(__name__)


#index route
    @app.route('/')
    def index():
      return "Hello, this is PetFax!"


# pets index route
    @app.route('/pets')
    def pets(): 
      return 'These are our pets available for adoption!'
    
#register pet blueprint
    from . import pet 
    app.register_blueprint(pet.bp)

    return app
