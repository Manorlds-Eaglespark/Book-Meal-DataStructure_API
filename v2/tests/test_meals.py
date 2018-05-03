import unittest
import app
import json


class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

        self.meal = {
            'name': 'Rice and Beans',
            'price': '5000'
        }
        


    def test_all_meals(self):
        response = self.app.get('/meals/')
        data = json.loads(response.data)
        self.assertEqual(data['meals'], [
            {
                'id': 1,
                'name': 'Chips and Chicken',
                'price': '10000',
                'time_created': 'Wed May  2 16:29:35 2018'
            },
            {
                'id': 2,
                'name': 'Beef and Rice',
                'price': '25000',
                'time_created': 'Wed May  2 16:29:35 2018',
            },
            {
                'id': 3,
                'name': 'Chicken and Matooke',
                'price': '35000',
                'time_created': 'Wed May  2 16:29:35 2018',
            }
        ])
        self.assertEqual(response.status_code, 200)


    def test_add_meal(self):
        response = self.app.post('/meals/', data= json.dumps(self.meal), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)

    

    
if __name__ == "__main__":
    unittest.main()
