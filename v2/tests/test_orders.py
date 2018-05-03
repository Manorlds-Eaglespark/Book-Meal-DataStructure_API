import unittest
import app
import json


class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    order = [
            {
                'id': 0,
                'meal_id': 4,
                'time_created': 'Wed May  2 16:49:35 2018',
                'time_expiration': 'Wed May  2 16:59:35 2018'
            }
        ]


    def test_orders(self):
        response = self.app.get('/orders')
        data = json.loads(response.data)
        self.assertEqual(data['orders'], [
            {
                'id': 1,
                'user_id': 10,
                'meal_id': 4,
                'time_created': 'Wed May  2 16:39:35 2018',
                'time_expiration': 'Wed May  2 16:49:35 2018'

            },
            {
                'id': 2,
                'user_id': 11,
                'meal_id': 7,
                'time_created': 'Wed May  2 16:39:35 2018',
                'time_expiration': 'Wed May  2 16:49:35 2018'
            }
        ])
        self.assertEqual(response.status_code, 200)

    def test_modify_order(self):
        response = self.app.put('/orders/2')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)


    def test_select_order(self):
        response = self.app.get('/orders/1')
        data = json.loads(response.data)
        self.assertEqual(data, {
                'id': 1,
                'user_id': 10,
                'meal_id': 4,
                'time_created': 'Wed May  2 16:39:35 2018',
                'time_expiration': 'Wed May  2 16:49:35 2018'

            }

        ) 
        self.assertEqual(response.status_code, 200)



if __name__ == "__main__":
    unittest.main()
