



users = [
    {
        "id": 0,
        "name": "Bob",
        "email": "bob@gmail.com", 
        "password": "xxy210",
        "login_status": "logged_out"
    },
    {
        "id": 1,
        "name": "Frank Kizamba",
        "email": "kizamba@gmail.com", 
        "password": "xxppzulu210",
        "login_status": "logged_out"
    }
]

meals = [
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
]

orders = [
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
        ]

order = [
    {
        'id': 1,
        'user_id': 10,
        'meal_id': 4,
        'time_created': 'Wed May  2 16:39:35 2018',
        'time_expiration': 'Wed May  2 16:49:35 2018'

    }
]

menus = [
    {
        'id': 0,
        'meal_ids': '1,2',
        'time_created': '2018-05-01 17:13:38'
    },
    {
        'id': 1,
        'meal_ids': '3',
        'time_created': '2018-05-04 17:13:38'
    },
    {
        'id': 2,
        'meal_ids': '3,2',
        'time_created': '2018-05-05 17:13:38'
    },
     {
        'id': 3,
        'meal_ids': '2,3',
        'time_created': '2018-05-06 17:13:38'
    }
]


# menu = [menu for menu in menus if menu ['id'] == 1 ] 

