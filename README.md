
# Warewise

Warewise is a Flask-based web application designed for efficient warehouse and inventory management. It allows users to manage suppliers and products seamlessly, featuring capabilities such as adding, editing, and deleting products and suppliers.

## Features

- **Manage Products**: Add, edit, and delete products.
- **Manage Suppliers**: Add, edit, and view suppliers, including the products they supply.
- **Inventory Tracking**: Keep track of product quantities and prices.
- **Dynamic Updates**: Update supplier contact information and product details in real-time.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have Python installed on your system, ideally Python 3.8 or newer. The project also requires Flask and SQLAlchemy.

### Installing

First, clone the repository to your local machine:

```bash
git clone https://github.com/psap2/Warewise.git
cd Warewise

1. **Set up a virtual environment** (optional but recommended):

```bash
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

2. **Install the required packages**:

```bash
pip install -r requirements.txt
```

3. **Initialize the database** (if applicable):

```bash
flask db upgrade 
```

4. **Start the server**:

```bash
flask run
```

Navigate to `http://127.0.0.1:5000/` in your browser to see the application in action.

## Built With

- [Flask](http://flask.pocoo.org/) - The web framework used
- [SQLAlchemy](https://www.sqlalchemy.org/) - Database ORM
- [Bootstrap](https://getbootstrap.com/) - Frontend framework for styling

