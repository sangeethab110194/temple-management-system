from app import create_app
from extensions import db
from models.admin import Admin


app=create_app()



with app.app_context():
  

    
        admin=Admin(username="admin")
        admin.set_password("admin123")
        print("Hash:", admin.password_hash)

        db.session.add(admin)
        db.session.commit()
        print("Admin craeted successfully")