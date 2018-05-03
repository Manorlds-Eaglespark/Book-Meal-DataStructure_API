"""This is the API file for the Book-A-Meal application"""
import time
import dummy_data
from models.meal import Meal
from models.menu import Menu
from models.order import Order
from flask import Flask, jsonify, request


app = Flask(__name__)


#Save a new user to make a signup
@app.route('/auth/signup', methods=['POST'])
def signup():
    """Method for creation of new user on the system"""
    name = str(request.get_json().get('name'))
    email = str(request.get_json().get('email'))
    password = str(request.get_json().get('password'))
    
    #add new user
    if name and email and password:
        new_user = {
            'id': len(users),
            'name': name,
            'email': email,
            'password': password,
            'login_status':'logged_in'
        }
        dummy_data.users.append(new_user)

        response = jsonify({
            "message":"Account created, 200 OK"
            })
        response.status_code = 201
        return response
    #return None


#Save a new user to make a signup
@app.route('/auth/login', methods=['POST'])
def login():
    """Logging in user"""
    email = str(request.get_json().get('email'))
    password = str(request.get_json().get('password'))

    emails, passwords = [], []    
    for user in dummy_data.users:
        emails.append(user['email'])
        passwords.append(user['password'])

    if email in emails and password in passwords:
        dummy_data.users[emails.index(email)]['login_status'] = "logged_in"
        response = jsonify({
            "message":"User successfully logged in",
            "status": "200, ok",
            "Login status": users[emails.index(email)]['login_status']
            })
        response.status_code = 200
        return response
    #return None




#Meals

@app.route('/meals/', methods=['GET'])
def get_all_meals():
    """This method returns all meals stored in the system"""
    return Meal.all_meals()



@app.route('/meals/', methods=['POST'])
def add_a_meal():
    """A Method to add a meal to the system"""
    name = str(request.get_json().get('name'))
    price = str(request.get_json().get('price'))
    
    if len(name) <= 0 or len(price) <=0:
        return Meal.bad_request()
    meal = Meal(name=name,price=price)
    if not meal:
        return Meal.bad_request()
    return Meal.meal_created_response()
    


@app.route('/meals/<int:meal_id>', methods=['PUT'])
def modify_meal(meal_id):
    """Method to modify an Meal"""
    name = str(request.get_json().get('name'))
    price = str(request.get_json().get('price'))
    if name and price:
        return Meal.update_meal(meal_id, name, price)
    return Meal.bad_request()



@app.route('/meals/<int:meal_id>', methods=['DELETE'])
def delete_meal(meal_id):
    """Method to modify an Meal"""
    return Meal.delete_meal(meal_id)

#Orders

@app.route('/orders/<int:order_id>', methods=['GET'])
def select_order(order_id):
    """Method that selects a meal to an order"""
    return Order.get_order(order_id)
    

@app.route('/orders', methods=['GET'])
def get_orders():
    """A Method that returns all the orders made"""
    return jsonify({'orders': dummy_data.orders})



@app.route('/orders', methods=['POST'])
def make_order():
    """A Method to make a new Order"""
    meal_id = request.get_json().get('meal_id')
    user_id = request.get_json().get('user_id')
    
    if not  int(meal_id) or not int(user_id):
        return Order.bad_order_request()

    order = Order.add_order(meal_id, user_id)
    
    if not order:
        return Order.bad_order_requestbad_request()
    return Order.order_created_response()





@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    """Method to modify an Order"""
    meal_id = str(request.get_json().get('meal_id'))
    if not meal_id:
        return Order.bad_order_request()
    modify = Order.modify_order(order_id, meal_id)
    if not modify:
        return Order.bad_order_request()
    return Order.order_modified_response()
    




#Menu

@app.route('/menu/', methods=['GET'])
def get_menu():
    """A Method to return the menu for the day"""
    return Menu.get_today_menu()

 


@app.route('/menu/', methods=['POST'])
def create_menu():
    """Method to create a menu for that day"""
    meal_ids = str(request.get_json().get('meal_ids'))
    return Menu.create_menu_item(meal_ids)
    


if __name__ == '__main__':
    app.run(host='localhost', port=5004, debug=True)
    
