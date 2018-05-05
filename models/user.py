import time
import random
from flask import jsonify
import dummy_data
import re

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
            EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
            if not EMAIL_REGEX.match(email):
                  return False 

            if len(password) < 3:
                  return False 
            
            if not name.replace(" ","").isalpha():
                  return False

            new_user = {
                  'id': random.randint(0, 1001),
                  'name': name,
                  'email': email,
                  'password': password,
                  'login_status':'logged_in'
                  }
            dummy_data.users.append(new_user)
            return True

      @staticmethod
      def login_user(email, password):

            EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
            if not EMAIL_REGEX.match(email):
                  response = jsonify(
                        {
                              "message":"Please enter a valid email"
                        })
                  response.status_code = 400
                  return response

            emails, passwords = [], []    
            for user in dummy_data.users:
                  emails.append(user['email'])
                  passwords.append(user['password'])

            if email in emails and password in passwords:
                  dummy_data.users[emails.index(email)]['login_status'] = "logged_in"
                  response = jsonify(
                        {
                              "message":"User successfully logged in",
                              "status": "200, ok",
                              "Login status": dummy_data.users[emails.index(email)]['login_status']
                        })
                  response.status_code = 200
                  return response
            response = jsonify(
                        {
                              "message":"Please provide valid login credentials"
                        })
            response.status_code = 400
            return response
