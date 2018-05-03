import time
import random
import dummy_data
from dummy_data import meals
from flask import Flask, jsonify, request


class Meal:
   
   #Constructor
    def __init__(self, name, price):
      self.id = random.randint(1001)
      self.name = name
      self.price = price
      self.time_created = time.asctime(time.localtime(time.time()))
      self.add_meal(self.id,self.name,self.price,self.time_created)

    def all_meals():
        response =  jsonify({'meals': dummy_data.meals})
        response.status_code = 200
        return response

    def add_meal(self, id, name, price, time_created):
            global meals
            new_meal = {
                'id': id,
                'name': name,
                'price': price,
                'time_created': time_created 
            }
            meals.append(new_meal)
            return True

        
    def bad_request():
        response =  jsonify({
            "message": "Bad request"
            })
        response.status_code = 400
        return response

    def meal_created_response():
        response =  jsonify({
            "message": "Meal Added"
            })
        response.status_code = 201
        return response



        

    def update_meal(id, name, price):
        meal_ids = []    
        for meal in dummy_data.meals:
            meal_ids.append(meal['id'])
        if id in meal_ids:
            dummy_data.meals[meal_ids.index(id)]['name'] = name
            dummy_data.meals[meal_ids.index(id)]['price'] = price
            dummy_data.meals[meal_ids.index(id)]['time_created'] = time.asctime(time.localtime(time.time()))

            response = jsonify({
                "Message":"Meal details updated." 
            }) 
            response.status_code = 200
            return response
        return bad_request()

        

    def delete_meal(id):
        meal_ids = []    
        for meal in dummy_data.meals:
            meal_ids.append(meal['id'])
        if id in meal_ids:
            del dummy_data.meals[meal_ids.index(id)]
            response = jsonify({
                "message":"meal deleted"
                })
            response.status_code = 401  #resource deleted code
            return response
        return bad_request()