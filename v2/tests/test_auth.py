import unittest
import app
import json
import re


class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()
        self.userr = {
                        "name": "Bob",
                        "email": "bob@gmail.com", 
                        "password": "xxy210"
                     }
        self.user_details = {
                                "email": "bob@gmail.com", 
                                "password": "xxy210",
                            }


    
    def test_signup_new_user(self):
        """"Test API to create a new user"""
        response = self.app.post('/auth/signup', data= json.dumps(self.userr), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('User created', data['message'])

    
    def test_wrong_details(self):
        userr = {
            "email": "vsdfsds@dfdf.com", 
            "password": "fdsfsf"
        }
        """"Test API to create a new user"""
        response = self.app.post('/auth/login', data= json.dumps(userr), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)


    def test_empty_details(self):
        userr = {
            "name": "",
            "email": "", 
            "password": ""
        }
        """"Test API to create a new user"""
        response = self.app.post('/auth/signup', data= json.dumps(userr), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)

    def test_signup_with_invalid_email(self):
        user_d = {
            "name":"Timothy",
            "email":"kyadondo",
            "password":"xyz123"
        }
        """"Test API for signning up user with wrong email"""
        response = self.app.post('/auth/signup', data= json.dumps(user_d), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        

    def test_login_with_invalid_email(self):
        user_d = {
            "email":"kyadondo",
            "password":"xyz123"
        }
        """"Test API for logging in up user with wrong email"""
        response = self.app.post('/auth/login', data= json.dumps(user_d), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        
    def test_signup_with_alpha_numeric_name(self):
        user_d = {
            "name":"Timothy565",
            "email":"kyadondo",
            "password":"xyz123"
        }
        response = self.app.post('/auth/signup', data= json.dumps(user_d), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)

    def test_login_user(self):
        """"Test API for logging in user"""
        response = self.app.post('/auth/login', data= json.dumps(self.user_details), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('200, ok', data['status'])


if __name__ == "__main__":
    unittest.main()
