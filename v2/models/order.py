import time
import random
from dummy_data import orders
import dummy_data
from flask import Flask, jsonify, request

class Order:
   
   #constructor
  def __init__(self, id, meal_id, user_id, time_created, time_expiration):
      self.id = id
      self.meal_id = meal_id
      self.user_id = user_id
      self.time_created = time.asctime(time.localtime(time.time()))
      self.time_expiration = time.asctime(time.localtime(time.time()  + 600))
    #  self.add_order(self.id,self.meal_id,self.user_id,self.time_created, self.time_expiration)



  def add_order(self):
    global orders
    new_order = {
        'id': self.id,
        'meal_id': self.meal_id,
        'user_id': self.user_id,
        'time_created': self.time_created, 
        'time_expiration': self.time_expiration
    }
    orders.append(new_order)
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
    
