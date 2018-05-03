import unittest
import app
import json


class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()
    

    def test_orders(self):
        response = self.app.get('/orders')
        data = json.loads(response.data)
        self.assertEqual(data['orders'], [
             {
                 'id': 1,
                 'user_id': 10,
                 'meal_id': 4,
                 'time_created': 'Monday, 14th February 2018'
             },
             {
                 'id': 2,
                 'user_id': 11,
                 'meal_id': 7,
                 'time_created': 'Monday, 14th February 2018'
             }
        ])
        self.assertEqual(response.status_code, 200)



        
        order = [
                    {
                        'id': 1,
                        'meal_id': 4,
                        'time_created': 'Monday, 14th February 2018'
                    }
                ]

    def test_select_order(self):
        response = self.app.get('/orders/1')
        data = json.loads(response.data)
        """ self.assertEqual(data['order'], 
             {
                 'order': 1
             }
        ) """
        self.assertEqual(response.status_code, 200)



if __name__ == "__main__":
    unittest.main()
