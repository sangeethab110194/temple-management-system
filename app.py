from flask import Flask
from flask_cors import CORS
from extensions import db,jwt
from flask_jwt_extended import JWTManager
import os



def create_app():
     app=Flask(__name__)
     basedir=os.path.abspath(os.path.dirname(__file__))
     app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///" + os.path.join(basedir,"instance","temple.db")
     app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
     app.config["JWT_SECRET_KEY"]="secret-key"

     db.init_app(app)
     jwt.init_app(app)
     CORS(app, resources={r"/api/*":{"origins":"*"}})

     from routes.auth import auth_bp
     from routes.receipt import receipt_bp
     from routes.report import report_bp
     app.register_blueprint(auth_bp, url_prefix="/api")
     app.register_blueprint(receipt_bp, url_prefix="/api/receipt")
     app.register_blueprint(report_bp, url_prefix="/api/reports")

     with app.app_context():
         db.create_all()

     return app  
if __name__ == "__main__":
     app=create_app()
     app.run(debug=True)

 

      

