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
        self.edit_meal = {
            'name': 'Potato chips plain',
            'price': '6000'
        }
        


    def test_all_meals(self):
        response = self.app.get('/meals/')
        data = json.loads(response.data)
        """ self.assertEqual(data['meals'], [
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
        ])  """
        self.assertEqual(response.status_code, 200)


    def test_add_meal(self):
        response = self.app.post('/meals/', data= json.dumps(self.meal), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)

    def test_modify_meal(self):
        response = self.app.put('/meals/2', data= json.dumps(self.edit_meal), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['Message'], "Meal details updated.")

    def test_delete_meal(self):
        response = self.app.delete('/meals/1')
        data = json.loads(response.data)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], "meal deleted")
    

    
if __name__ == "__main__":
    unittest.main()
