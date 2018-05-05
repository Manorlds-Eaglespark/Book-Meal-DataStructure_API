import time
import random
from dummy_data import orders
import dummy_data
from flask import Flask, jsonify, request

class Order:
   
   #constructor
  def __init__(self, meal_id, user_id):
      self.id = random.randint(0,1001)
      self.meal_id = meal_id
      self.user_id = user_id
      self.time_created = time.asctime(time.localtime(time.time()))
      self.time_expiration = time.asctime(time.localtime(time.time()  + 600))
      #self.add_order(self.id,self.meal_id,self.user_id,self.time_created, self.time_expiration)


  @staticmethod
  def add_order(meal_id, user_id):
    global orders
    new_order = Order(meal_id, user_id)
    n_order = {
        'id': new_order.id,
        'user_id': new_order.user_id,
        'meal_id': new_order.meal_id,
        'time_created': new_order.time_created, 
        'time_expiration': new_order.time_expiration
    }
    orders.append(n_order)
    return True

  @staticmethod
  def modify_order(id, meal_id):
    global orders
    order_ids = []    
    for order in dummy_data.orders:
      order_ids.append(order['id'])
    if id in order_ids:
      orders[order_ids.index(id)]['meal_id']  = meal_id
      orders[order_ids.index(id)]['time_created']  = time.asctime(time.localtime(time.time()))
      orders[order_ids.index(id)]['time_expiration']  = time.asctime(time.localtime(time.time() + 600))
      return True


  @staticmethod
  def order_modified_response():
    response = jsonify({
      "message":"Order modified",
      "status": "200, OK"
    })
    response.status_code = 200
    return response

  @staticmethod
  def order_created_response():
    response = jsonify({
      "message":"Order Created",
      "status": "200, OK"
    })
    response.status_code = 200
    return response
    
  @staticmethod
  def get_order(order_id):
    all_orders = []    
    for order in dummy_data.orders:
        all_orders.append(order['id'])
    if order_id not in all_orders:
      response = jsonify({
        "message":"Order not in the system"
      })
      response.status_code = 400
      return response

    if order_id in all_orders:
        response =  jsonify({
            "id": dummy_data.orders[all_orders.index(order_id)]['id'],
            "meal_id": dummy_data.orders[all_orders.index(order_id)]['meal_id'],
            "user_id": dummy_data.orders[all_orders.index(order_id)]['user_id'],
            "time_created": dummy_data.orders[all_orders.index(order_id)]['time_created'],
            "time_expiration": dummy_data.orders[all_orders.index(order_id)]['time_expiration']
            })
        response.status_code = 200
        return response
