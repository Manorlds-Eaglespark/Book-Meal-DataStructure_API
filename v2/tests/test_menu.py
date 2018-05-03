import unittest
import app
import json


class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

        self.today_meals = {
            "meal_ids":"1,2"
        }

    

    def test_today_menu(self):
        response = self.app.get('/menu/')
        data = json.loads(response.data)
        self.assertEqual(data['meal_ids'], [1,2] )
        self.assertEqual(response.status_code, 200)
    

    def test_create_today_menu(self):
        "Testing creation of a menu"    
        response = self.app.post('/menu/', data= json.dumps(self.today_meals), content_type='application/json')
        data = json.loads(response.data)
        self.assertIn("Today's menu has been updated", data['message'])
        self.assertEqual(response.status_code, 200)    

if __name__ == "__main__":
    unittest.main()
