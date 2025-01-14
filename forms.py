from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, IntegerField, SubmitField, PasswordField
from wtforms.validators import DataRequired, NumberRange, Email, EqualTo

class ProductForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(message="Please enter a product name.")])
    id = IntegerField('ID', validators=[DataRequired(message="Please enter product id."), NumberRange(min=0, message="ID cannot be negative")])
    price = DecimalField('Price', validators=[DataRequired(message="Please enter a price."),
                                              NumberRange(min=0, message="Price cannot be negative.")])
    quantity = IntegerField('Quantity', validators=[DataRequired(message="Please enter a quantity."),
                                                    NumberRange(min=0, message="Quantity cannot be negative.")])
    supplier_id = IntegerField('Supplier ID', validators=[DataRequired(message="Please enter supplier's id."), NumberRange(min=0, message="ID cannot be negative")])

    
    submit = SubmitField('Add Product')

class SupplierForm(FlaskForm):
    id = IntegerField('ID', validators=[DataRequired(message="Please enter supplier id."), NumberRange(min=0, message="ID cannot be negative")])
    name = StringField('Name', validators=[DataRequired(message="Please enter name of supplier.")])
    contact_info = StringField('Contact', validators=[DataRequired(message="Please provide an email for the supplier.")])
    submit = SubmitField('Add Supplier')

class NewUserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message="Please enter a username")])
    email = StringField('Email', validators=[DataRequired(message="Please enter a proper email."), Email()])
    password = PasswordField('Password', validators=[DataRequired(message="Please enter a password")])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(message="Confirm password does not match"), EqualTo('password')])
    submit = SubmitField('Register')
