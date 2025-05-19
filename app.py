from flask import Flask, render_template
from controllers.database import db
from controllers.config import Config
from controllers.models import *
from controllers.test_routes import *


# from flask_sqlalchemy import SQLAlchemy

# # Creating a instance of SqlAlchemy class
# db = SQLAlchemy()

def create_app():

    app = Flask(__name__,template_folder='template')
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///grocery_store.sqlite3'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['SECRET_KEY'] = 'your_secret_key_here'
    app.config.from_object(Config)





    #tell database to use paritcular app
    db.init_app(app)

    # # creating models for the database
    # class User(db.Model):
    #     # 'user'
    #     user_id = db.Column(db.Integer, autoincrement= True, primary_key=True)
    #     email = db.Column(db.String, unique= True, nullable=False)
    #     password = db.Column(db.String, nullable= False)
    #     mobile_number = db.Column(db.String, default = "0000000000")
    #     address= db.Column(db.String)
    #     dob = db.Column(db.Date)

    #     role = db.relationship('Role', secondary = 'user_role', backref = 'users')  #[<objet1>, <obj2>]
    
    # class Role(db.Model):
    #     # 'role'
    #     role_id = db.Column(db.Integer, primary_key = True)
    #     role_name = db.Column(db.String, unique= True, nullable=False)

    # class UserRole(db.Model):
    #     # 'user_role'
    #     id = db.Column(db.Integer, primary_key = True)
    #     user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    #     role_id = db.Column(db.Integer, db.ForeignKey('role.role_id'))


    # class Category(db.Model):
    #     # 'category'
    #     category_id = db.Column(db.Integer, primary_key = True)
    #     category_name = db.Column(db.String, unique= True, nullable=False)
    #     category_description = db.Column(db.String)

    # class Product(db.Model):
    #     # 'product'
    #     product_id = db.Column(db.Integer, primary_key = True)
    #     product_name = db.Column(db.String, unique= True, nullable=False)
    #     product_description = db.Column(db.String)
    #     product_price = db.Column(db.Float)
    #     category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'))

    #     category = db.relationship('Category', backref = 'products')

    with app.app_context():
        db.create_all()

        # First Approch -- Without using Relationship

        # admin = User.query.all()
        
        # admin = User.query.filter_by(email = "admin@gmail.com").first()
        # if not admin:
        #     admin_user = User(
        #         email = "admin@gmail.com",
        #         password="admin1234",
        #     )
        #     db.session.add(admin_user)

        # admin_role = Role.query.filter_by(role_name = "admin").first()
        # if not admin_role:
        #     admin_role = Role(
        #         role_name = "admin"
        #     )
        #     db.session.add(admin_role)

        # user_role = Role.query.filter_by(role_name = "user").first()
        # if not user_role:
        #     user_role = Role(
        #         role_name = "user"
        #     )
        #     db.session.add(user_role)

        # admin = User.query.filter_by(email = "admin@gmail.com").first()
        # #admin is object of class User
        # get_role_id = Role.query.filter_by(role_name = "admin").first()
        # #get_role_id is object of class Role
        # user_role_defined = UserRole.query.filter_by(user_id = admin.user_id).first()
        # if not user_role_defined:
        #     user_role_defined = UserRole(
        #         user_id = admin.user_id,
        #         role_id = get_role_id.role_id
        #     )
        #     db.session.add(user_role_defined)

        # second Approch -- using Relationship

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


# @app.route('/')
# def hello_world():
#     return f'Hello, World! {6} + {7} = {6 + 7}'


# # /hello/john

# @app.route('/hello/<int:age>')
# def hello(age):
#     list_students = [
#         {'name': 'John', 'age': 20},
#         {'name': 'Jane', 'age': 22},
#         {'name': 'Bob', 'age': 19},
#         {'name': 'Alice', 'age': 21},
#         {'name': 'Charlie', 'age': 23},
#         {'name': 'David', 'age': 24},
#         {'name': 'Eve', 'age': 25},
#         {'name': 'Frank', 'age': 26},
#         {'name': 'Grace', 'age': 27},
#         {'name': 'Heidi', 'age': 28}
#     ]
#     search_result =[]
#     for student in list_students:
#         if student['age'] > age:
#             search_result.append(student)

#     return render_template('home.html', students = search_result)


if __name__ == '__main__':
    app.run(debug=True)