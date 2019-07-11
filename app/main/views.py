from flask import render_template
from app import app

@app.route('/')
def index():
    '''
    View the home page (to be added from landing page syntax)
    '''
    
    # children =b.get_b('children')
    # men =b.get_b('men')
    # women =b.get_b('women')
    return render_template('cart.html')
# @main.route('/b/children')
# def children():
#     b=b.get_b('children')
#     return render_template('children.html',b=b)
# @main.route('/b/men')
# def men():
#     b = b.get_b('men')
#     return render_template('men',b=b)
# @main.router('/b/women')
# def women():
#     b = b.get_b('women')
#     return render_template('women',b=b)
    
# @app.route("/cart/add", methods=['POST'])
# def add_to_cart():
#     cart = ShoppingCart.add(product=request.form['product'], quantity=int(request.form['quantity']))
#     return jsonify(cart)
# @app.route("/cart")
# def view_cart():
#     cart = ShoppingCart.get()
#     return render_template("cart.html", cart=cart)
# @app.route("/cart/remove/<item_id>", methods=['POST'])
# def remove_from_cart(item_id):
#     cart = ShoppingCart.remove(item_id)
#     return jsonify(cart)
