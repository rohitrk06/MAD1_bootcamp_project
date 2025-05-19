from flask import Flask, render_template
from controllers.database import db
from controllers.config import Config
from controllers.models import *

def create_app():
    app = Flask(__name__,template_folder='template')
    app.config.from_object(Config)
    db.init_app(app)
    with app.app_context():
        db.create_all()
        admin_role = Role.query.filter_by(role_name = "admin").first()
        if not admin_role:
            admin_role = Role(
                role_name = "admin"
            )
            db.session.add(admin_role)

        user_role = Role.query.filter_by(role_name = "user").first()
        if not user_role:
            user_role = Role(
                role_name = "user"
            )
            db.session.add(user_role)

        
        admin = User.query.filter_by(email = 'admin@gmail.com').first()
        if not admin:
            admin_user = User(
                email = "admin@gmail.com",
                password="admin1234",

                role = [admin_role, user_role]
            )
            db.session.add(admin_user)
        db.session.commit()
    return app

app = create_app()

from controllers.test_routes import *
from controllers.auth_routes import *

if __name__ == '__main__':
    app.run(debug=True)