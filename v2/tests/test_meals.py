import unittest
import app
import json


class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()
        


    def test_all_meals(self):
        response = self.app.get('/meals/')
        data = json.loads(response.data)
        self.assertEqual(data['meals'], [
             {
                    'id': 1,
                    'name': 'Beef and Rice',
                    'price': '25000',
                    'time_created': 'Monday, 14th February 2018'
                },
                {
                    'id': 2,
                    'name': 'Chicken and Matooke',
                    'price': '35000',
                    'time_created': 'Monday, 14th February 2018'
                }
        ])
        self.assertEqual(response.status_code, 200)
    

    
if __name__ == "__main__":
    unittest.main()
