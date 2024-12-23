from flask import Flask, request, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from forms import ProductForm, SupplierForm, NewUserForm
from models import Product, Supplier, Users, db
import secrets
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = secrets.token_hex(16)

db.init_app(app)

#Adding authentication to our app with Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

##
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = NewUserForm()

    if form.validate_on_submit():  
        
        existing_user = Users.query.filter((Users.username == form.username.data) | (Users.email == form.email.data)).first()

        if existing_user:
            flash('A user with this username/email already exists', 'error')
            return render_template('register.html', form=form)

        username = form.username.data
        email = form.email.data
        password = form.password.data
        new_user = Users(username=username, email=email, password=password)
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash('Failed to register user due to an error: {}'.format(e), 'error')
            return render_template('register.html', form=form)
        
    elif request.method == 'GET':
        return render_template('register.html', form=form)



@app.route('/')
def index():
    # Displays the homepage
    return render_template('index.html')

@app.route('/products')
def view_products():
    # Display all products. 
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/suppliers')
def view_suppliers():
    # Display all suppliers.
    suppliers = Supplier.query.all()
    return render_template('index.html', suppliers=suppliers)


@app.route('/product/new', methods=['GET', 'POST'])
def add_product():
    # Handle adding a new product.
    form = ProductForm()
    if form.validate_on_submit():  
        id = form.id.data
        existing_product = Product.query.get(id)
        if existing_product:
            flash('This product already exists', 'error')
            return render_template('product_form.html', form=form)
    
        name = form.name.data
        quantity = form.quantity.data
        price = form.price.data
        supplier = form.supplier_id.data
        new_product = Product(id=id, name=name, quantity=quantity, price=price, supplier_id=supplier)

        try:
            db.session.add(new_product)
            db.session.commit()
            return redirect(url_for('index'))  
        except Exception as e:
            db.session.rollback()
            flash('Failed to add supplier due to an error: {}'.format(e), 'error')
            return render_template('product_form.html', form=form)
        
    elif request.method == 'GET':
        return render_template('product_form.html', form=form)
    

@app.route('/supplier/new', methods=['GET', 'POST'])
def add_supplier():
    # Handle adding a new supplier.
    # Create a new Supplier instance from form data and add it to the database.
    form = SupplierForm()

    if form.validate_on_submit():  
        id = form.id.data
        existing_supplier = Supplier.query.get(id)
        if existing_supplier:
            flash('This supplier already exists', 'error')
            return render_template('supplier_form.html', form=form)

        name = form.name.data
        contact_info = form.contact_info.data
        new_supplier = Supplier(id=id, name=name, contact_info=contact_info)

        try:
            db.session.add(new_supplier)
            db.session.commit()
            return render_template('index.html') 
        except Exception as e:
            db.session.rollback()
            flash('Failed to add supplier due to an error: {}'.format(e), 'error')
            return render_template('supplier_form.html', form=form)
        
    elif request.method == 'GET':
        return render_template('supplier_form.html', form=form)


@app.route('/product/<int:id>/edit', methods=['GET', 'POST'])
def edit_product(id):
    product = Product.query.get_or_404(id)  
    form = ProductForm(obj=product)

    if form.validate_on_submit():
        product.name = form.name.data  
        product.quantity = form.quantity.data
        product.price = form.price.data

        try:
            db.session.commit()  
            flash('Product updated successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash('Error updating product: {}'.format(e), 'error')
            return render_template('edit_product.html', form=form, product_id=id)

    return render_template('edit_product.html', form=form, product_id=id)

@app.route('/suppliers/<int:id>/edit', methods=['GET', 'POST'])
def edit_supplier(id):
    supplier = Supplier.query.get_or_404(id)  
    form = SupplierForm(obj=supplier)

    if form.validate_on_submit():
        supplier.name = form.name.data  
        supplier.contact_info = form.contact_info.data

        try:
            db.session.commit()  
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash('Error updating supplier: {}'.format(e), 'error')
            return render_template('edit_supplier.html', form=form, supplier_id=id)

    return render_template('edit_supplier.html', form=form, supplier_id=id)


@app.route('/product/<int:id>/delete', methods=['POST'])
def delete_product(id):
    product = Product.query.get_or_404(id)  
    try:
        db.session.delete(product)  
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting product: {e}', 'error')

    return render_template('index.html')


@app.route('/suppliers/<int:id>/delete', methods=['POST'])
def delete_supplier(id):
    supplier = Supplier.query.get_or_404(id)  
    try:
        db.session.delete(supplier)  
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting product: {e}', 'error')

    return render_template('index.html')

if __name__ == '__main__':

    with app.app_context():
        db.create_all() 

    app.run(debug=True)
