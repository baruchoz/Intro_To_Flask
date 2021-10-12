from app import app
from flask import render_template


# will return index.html file function file in our templates folder
@app.route('/')
def index():
    name = 'Baruch'
    title = 'Coding Temple Flask'
    return render_template('index.html', name_of_user=name, title=title)


# will return products.html file function file in our templates folder
@app.route('/products') 
def test():
    title = 'Coding Temple Products'
    products = ['apple', 'orange', 'banana', 'peach']
    return render_template('products.html', title=title, products=products)
