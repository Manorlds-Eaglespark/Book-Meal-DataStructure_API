import time
import random
from flask import jsonify
import dummy_data

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

      @staticmethod
      def login_user(email, password):
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
