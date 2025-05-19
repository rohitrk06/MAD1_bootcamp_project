from controllers.database import db

# creating models for the database
class User(db.Model):
    # 'user'
    user_id = db.Column(db.Integer, autoincrement= True, primary_key=True)
    email = db.Column(db.String, unique= True, nullable=False)
    password = db.Column(db.String, nullable= False)
    mobile_number = db.Column(db.String, default = "0000000000")
    address= db.Column(db.String)
    dob = db.Column(db.Date)

    role = db.relationship('Role', secondary = 'user_role', backref = 'users')  #[<objet1>, <obj2>]
  
class Role(db.Model):
    # 'role'
    role_id = db.Column(db.Integer, primary_key = True)
    role_name = db.Column(db.String, unique= True, nullable=False)

class UserRole(db.Model):
    # 'user_role'
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.role_id'))


class Category(db.Model):
    # 'category'
    category_id = db.Column(db.Integer, primary_key = True)
    category_name = db.Column(db.String, unique= True, nullable=False)
    category_description = db.Column(db.String)

class Product(db.Model):
    # 'product'
    product_id = db.Column(db.Integer, primary_key = True)
    product_name = db.Column(db.String, unique= True, nullable=False)
    product_description = db.Column(db.String)
    product_price = db.Column(db.Float)
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'))

    category = db.relationship('Category', backref = 'products')
