import unittest
import app
import json


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
    

    def test_login_user(self):
        """"Test API for logging in user"""
        response = self.app.post('/auth/login', data= json.dumps(self.user_details), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('200, ok', data['status'])


if __name__ == "__main__":
    unittest.main()
