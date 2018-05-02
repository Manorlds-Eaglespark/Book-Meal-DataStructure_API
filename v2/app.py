"""This is the API file for the Book-A-Meal application"""
import time
import dummy_data
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


@app.route('/orders/<int:order_id>', methods=['GET'])
def select_order(order_id):
    """Method that selects a meal to an order"""
    all_orders = []    
    for order in dummy_data.orders:
        all_orders.append(order['id'])
    if order_id in all_orders:
        response =  jsonify({
            "id": dummy_dataorders[all_orders.index(order_id)]['id'],
            "meal_id": dummy_data.orders[all_orders.index(order_id)]['meal_id'],
            "user_id": dummy_data.orders[all_orders.index(order_id)]['user_id'],
            "time_created": dummy_data.orders[all_orders.index(order_id)]['time_created'],
            "time_expiration": dummy_data.orders[all_orders.index(order_id)]['time_expiration']
            })
        response.status_code = 200
        return response


@app.route('/meals/', methods=['GET'])
def get_all_meals():
    """This method returns all meals stored in the system"""
    response = jsonify({'meals': dummy_data.meals}) 
    response.status_code = 200
    return response



@app.route('/meals/', methods=['POST'])
def add_a_meal():
    """A Method to add a meal to the system"""
    name = str(request.get_json().get('name'))
    price = str(request.get_json().get('price'))
    time_created = str(request.get_json().get('time_created'))
    if name and price and time_created:
        response = jsonify({
            "id": len(meals),
            "name": name,
            "price": price,
            "time_creatd": time.asctime(time.localtime(time.time())),
            "time_expiration": time.asctime(time.localtime(time.time() + 600))
            })
        response.status_code = 201
        return response
    #return None


@app.route('/orders', methods=['GET'])
def get_orders():
    """A Method that returns all the orders made"""
    return jsonify({'orders': orders})


@app.route('/orders', methods=['POST'])
def make_order():
    """A Method to make a new Order"""
    meal_id = request.get_json().get('meal_id')
    user_id = request.get_json().get('user_id')
    if meal_id and user_id:
        response = jsonify({
            'meal_id': meal_id,
            'user_id': user_id,
            'Expiration time': time.asctime(time.localtime( \
            time.time()  + 600))
            })
        response.status_code = 201
        return response
    #return None


@app.route('/order/<int:order_id>', methods=['PUT'])
#def modify_order(order_id):
def modify_order():
    """Method to modify an Order"""
    meal_id = str(request.get_json().get('meal_id'))
    response = jsonify({
        'new meal_id': meal_id,
        'date_created': "original created time",
        'date_updated': time.asctime(time.localtime(time.time()))
        })
    response.status_code = 200
    return response


@app.route('/menu/', methods=['GET'])
def get_menu():
    """A Method to return the menu for the day"""
    months_days = []
    for month_day in menus:
        months_days.append((month_day['time_created'][:10]))
    
    today_month_day =  (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))[:10]
    if today_month_day in months_days:
        response = jsonify({
             'id': menus[months_days.index(today_month_day)]['id'],
             'meal_ids': menus[months_days.index(today_month_day)]['meal_ids'],
             'time_created': menus[months_days.index(today_month_day)]['time_created']
        }) 
        response.status_code = 200
        return response
 


@app.route('/menu/', methods=['POST'])
def create_menu():
    """Method to create a menu for that day"""
    meal_ids = str(request.get_json().get('meal_ids'))

    meal_ids = meal_ids.split(",")
    for i in range(len(meal_ids)):
        #checking if digit
        if meal_ids[i].isdigit():
            meal_ids[i] = int(meal_ids[i])
        else:
            response = jsonify({
            'message': "Please add only integer values as ids",
            'status':  "400, Bad Request"
            })
            response.status_code = 400
            return response 
    
    system_meals = []
    for meal in dummy_data.meals:
        system_meals.append(int(meal['id']))

    for m_ids in meal_ids:
        if m_ids not in system_meals:
            response = jsonify({
            'message': "You added a meal not in the system",
            'status':  "400, Bad Request"
            })
        response.status_code = 400
        return response 
            
        todays_menu = {
            'id': len(dummy_data.menus),
            'meal_ids': meal_ids,
            'time_created': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        }
        menus.append(todays_menu)
   
        response = jsonify({
            'message': "Today's menu has been loaded",
            'status':  "201, created"
            })
        response.status_code = 201
        return response
    #return None



if __name__ == '__main__':
    app.run(host='localhost', port=5004, debug=True)
    
