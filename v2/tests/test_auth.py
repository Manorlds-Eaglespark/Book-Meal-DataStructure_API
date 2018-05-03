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


    
    def test_signup_new_user(self):
        """"Test API to create a new user"""
        response = self.app.post('/auth/signup', data= json.dumps(self.userr), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('Bob', data['name'])
    


if __name__ == "__main__":
    unittest.main()
