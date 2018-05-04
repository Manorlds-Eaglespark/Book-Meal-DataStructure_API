import time
import dummy_data
from models.meal import Meal
from flask import Flask, jsonify, request

def bad_Request():
      response =  jsonify({
                        "message": "Bad request"
                        })
      response.status_code = 400
      return response

class Menu:
   
      def __init__(self, mealIds):
            self.id = random.randint(1001)
            self.mealIds = mealIds
            self.time_created = time.time()



      def get_today_menu():
            months_days = []
            for month_day in dummy_data.menus:
                  months_days.append((month_day['time_created'][:10]))
    
            today_month_day =  (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))[:10]
            if today_month_day in months_days:
                  response = jsonify({
                        'id': dummy_data.menus[months_days.index(today_month_day)]['id'],
                        'meal_ids': dummy_data.menus[months_days.index(today_month_day)]['meal_ids'],
                        'time_created': dummy_data.menus[months_days.index(today_month_day)]['time_created']
                  }) 
                  response.status_code = 200
                  return response
            response =  jsonify({
                              "message": "Today's menu not set"
                              })
            response.status_code = 400
            return response

      def create_menu_item(meal_idz):
            meal_ids = meal_idz
            meal_ids = meal_ids.split(",")
            for i in range(len(meal_ids)):
                  #checking if digit
                  if not meal_ids[i].isdigit():
                        response = jsonify({
                        'message': "Please add only integer values as ids",
                        'status':  "400, Bad Request"
                        })
                        response.status_code = 400
                        return response
                  meal_ids[i] = int(meal_ids[i])
            
            system_meals, months_days = [], []
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


            for month_day in dummy_data.menus:
                  months_days.append((month_day['time_created'][:10]))
    
            today_month_day =  (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))[:10]
            if today_month_day in months_days:
                  meal_string = ""
                  for i in meal_ids:
                        meal_string += i+','
                  meal_string[len(meal_string)] = ''; 

                  dummy_data.menus[months_days.index(today_month_day)]['meal_ids'] = meal_string
                  dummy_data.menus[months_days.index(today_month_day)]['time_created'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                  
                  response = jsonify({
                        'message': "Today's menu has been set",
                        'status':  "200, updated"
                  }) 
                  response.status_code = 200
                  return response
    
            todays_menu = {
                  'id': len(dummy_data.menus),
                  'meal_ids': meal_idz,
                  'time_created': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            }
            dummy_data.menus.append(todays_menu)
      
            response = jsonify({
                  'message': "Today's menu has been set",
                  'status':  "201, created"
                  })
            response.status_code = 201
            return response
            

