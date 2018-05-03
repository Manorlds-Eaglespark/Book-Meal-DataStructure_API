import unittest
import app
import json


class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    

    def test_today_menu(self):
        response = self.app.get('/menu/')
        data = json.loads(response.data)
        self.assertEqual(data['menu'], [
                {
                    'id': 1,
                    'meal_ids': '4,2,5,6,7',
                    'time_created': 'Monday, 14th February 2018'
                }
                
        ])
        self.assertEqual(response.status_code, 200)
        

if __name__ == "__main__":
    unittest.main()
