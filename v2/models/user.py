import time
import random
from dummy_data import orders
import dummy_data
from flask import Flask, jsonify, request

class User:   
      #Constructor for the User object, for initialization
      def __init__(self, name, email):
            self.id = random.randint(0, 1001)
            self.name = name
            self.email = email
            self.admin_status = "false"
            self.time_created = time.time()

      @staticmethod
      def create_user(name, email, password):
            new_user = {
                  'id': random.randint(0, 1001),
                  'name': name,
                  'email': email,
                  'password': password,
                  'login_status':'logged_in'
                  }
            dummy_data.users.append(new_user)
            return True



