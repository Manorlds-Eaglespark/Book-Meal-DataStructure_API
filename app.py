"""This is the API file for the Book-A-Meal application"""
from flask import Flask, jsonify, request, session
from models.meal import Meal
from models.menu import Menu
from models.order import Order
from models.user import User
from functools import wraps
import dummy_data


app = Flask(__name__)

app.secret_key = "secretkey"

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not "test" in session:
            return "Unathorization access"
        return f(*args, **kwargs)
    return decorated_function



#Save a new user to make a signup
@app.route('/auth/signup', methods=['POST'])
def signup():
    """Method for creation of new user on the system"""
    name = str(request.get_json().get('name'))
    email = str(request.get_json().get('email'))
    password = str(request.get_json().get('password'))
    if not (name and email and password):
        response = jsonify({
            "message":"Please provide required details"
            })
        response.status_code = 400
        return response
    created_flag = User.create_user(name, email, password)
    if not created_flag:
        response = jsonify({
            "status":"User not created",
            "message":"invalid input: password too short, or \
            empty fields or invalid email. Please check again"
            })
        response.status_code = 400
        return response
    response = jsonify({
        "message":"User created",
        "status": "201, OK"
        })
    response.status_code = 201
    return response



#Save a new user to make a signup
@app.route('/auth/login', methods=['POST'])
def login():
    """Logging in user"""
    email = str(request.get_json().get('email'))
    password = str(request.get_json().get('password'))
    if not (email and password):
        response = jsonify({
            "message": "Enter required details correctly"
        })
        response.status_code = 400
        return response
    if email and password:
        session["test"] = True
        return User.login_user(email, password)

#Meals

@app.route('/meals/', methods=['GET'])
#@login_required
def get_all_meals():
    """This method returns all meals stored in the system"""
    return Meal.all_meals()

@app.route('/meals/<int:meal_id>', methods=['GET'])
def get_meal(meal_id):
    """Method to modify an Meal"""
    return Meal.get_meal(meal_id)


@app.route('/meals/', methods=['POST'])
def add_a_meal():
    """A Method to add a meal to the system"""
    name = str(request.get_json().get('name'))
    price = str(request.get_json().get('price'))

    if len(name) <= 0 and len(price) <= 0:
        return Meal.bad_request()
    meal = Meal.add_meal(name=name, price=price)
    print(meal)
    if not meal:
        return Meal.bad_request()
    return Meal.meal_created_response()
    
    

@app.route('/meals/<int:meal_id>', methods=['PUT'])
def modify_meal(meal_id):
    """Method to modify an Meal"""
    name = str(request.get_json().get('name'))
    price = str(request.get_json().get('price'))
    if not (name or price):
        response = jsonify({
                "message":"please add all details."
            })
        response.status_code = 400
        return response

    return Meal.update_meal(meal_id, name, price)
    


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




@app.route('/posts/', methods=['GET'])
def get_member_posts():
    return jsonify(
        [
    {
        "id":1,
        "name": "Joseph Omoding",
        "message": "God is so God, yesterday today and tomorrow",
        "image_url": "https://www.rainbowtoken.com/wp-content/uploads/2018/01/20-Bible-Verses-About-Strength-That-Will-Lift-Your-Soul.jpg",
        "created-at":"443423434234"
    },
    {
        "id":2,
        "name": "Ronald Mukisa",
        "message": "This is the way of the Lord",
        "image_url": "https://media.swncdn.com/cms/GODTUBE/60894-27804-10312015-psalm-23-4-social-1.jpg",
        "created-at":"443423434234"
    },
    {
        "id":3,
        "name": "Tom Kaweesa",
        "message": "We thank God for all the testimonies here",
        "image_url": "https://media.swncdn.com/cms/BST/54252-god-bible-verses.800w.tn.webp",
        "created-at":"443423434234"
    },
    {
        "id":4,
        "name": "Crystal Omubulizi",
        "message": "Christ is everything. He loved us first.",
        "image_url": "https://images.knowing-jesus.com/w/400/19-PSALMS/Psalm+103-5+He+Satisify+Your+Year+With+Good+Things+red.jpg",
        "created-at":"443423434234"
    }
]);


@app.route('/profiles/', methods=['GET'])
def get_church_profiles():
    return jsonify(
         [
        {
            "id":1,
            "name": "Life church",
            "location": "Kampala",
            "pastor": "the pastor's name",
            "service_time": "Sundays 8AM - 12PM",
            "contact":"443423434234"
        },
        {
            "id":2,
            "name": "Watoto",
            "location": "Kampala",
            "pastor": "the pastor's name",
            "service_time": "Sunday mornings",
            "contact":"455555453"
        },
        {
            "id":3,
            "name": "Bukoto C/U",
            "location": "Bukoto",
            "pastor": "the pastor's  name",
            "service_time": "Sunday mornings",
            "contact":"2343523432"
        },
        {
            "id":4,
            "name": "St. Balikudembe",
            "location": "Down town, Kampala",
            "pastor": "the pastor's name",
            "service_time": "Sunday mornings",
            "contact":"3456434"
        },
        {
            "id":5,
            "name": "Redeemed Church",
            "location": "Kalerwe",
            "pastor": "the pastor's name",
            "service_time": "Monday mornings",
            "contact":"2342342342"
        },
        {
            "id":6,
            "name": "St. Mathias Mulumba",
            "location": "Kireka",
            "pastor": "the pastor's name",
            "service_time": "Sunday mornings",
            "contact":"4355654343"
        }
    ]
    
    );



if __name__ == '__main__':
    app.run(host='localhost', port=5004, debug=True)
