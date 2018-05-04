import unittest
import app
import json


class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

        self.today_meals = {
            "meal_ids":"1,2"
        }

        self.meals_not = {
            "meal_ids":"10,8,27"
        }

        self.meals_not_ints = {
            "meal_ids":"a,b,27"
        }

    

    def test_today_menu(self):
        response = self.app.get('/menu/')
        data = json.loads(response.data)
        self.assertIn(data['meal_ids'], '4,2,5,6,7' )
        self.assertEqual(response.status_code, 200)
    

    """  def test_create_today_menu(self):
        "Testing creation of a menu"    
        response = self.app.post('/menu/', data= json.dumps(self.today_meals), content_type='application/json')
        data = json.loads(response.data)
        self.assertIn("Today's menu has been set", data['message'])
        self.assertEqual(response.status_code, 201)  """

    def test_create_today_menu_meals_not_available(self):
        "Testing if meals not in system"  
        response = response = self.app.post('/menu/', data= json.dumps(self.meals_not), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400) 
        
    def test_create_today_non_integers_entered(self):
        "Testing if meals not ints"  
        response = response = self.app.post('/menu/', data= json.dumps(self.meals_not_ints), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)   

if __name__ == "__main__":
    unittest.main()
