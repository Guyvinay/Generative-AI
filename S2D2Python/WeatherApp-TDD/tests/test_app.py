# tests/test_app.py (update the file)
import unittest
import json
from app import app

class WeatherAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_add_city(self):
        data = {
            'city': 'Chicago',
            'current': {'temperature': 18, 'weather': 'Partly Cloudy'},
            'forecast': [
                {'temperature': 19, 'weather': 'Partly Cloudy'},
                {'temperature': 20, 'weather': 'Clear'},
                # Add more forecast entries for future days
            ]
        }
        response = self.app.post('/weather/', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn(b"City added successfully", response.data)

    def test_add_invalid_city(self):
        data = {
            'current': {'temperature': 18, 'weather': 'Partly Cloudy'},
            'forecast': [
                {'temperature': 19, 'weather': 'Partly Cloudy'},
                {'temperature': 20, 'weather': 'Clear'},
            ]
        }
        response = self.app.post('/weather/', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_add_invalid_weather_data(self):
        data = {
            'city': 'Chicago',
            'current': {'temperature': 18, 'weather': 'Partly Cloudy'},
        }
        response = self.app.post('/weather/', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()

# # tests/test_app.py (update the file)

# # tests/test_app.py (update the file)
# import unittest
# import json
# from app import app

# class WeatherAppTestCase(unittest.TestCase):

#     def setUp(self):
#         self.app = app.test_client()

#     def test_weather_endpoint(self):
#         response = self.app.get('/weather/San Francisco')
#         self.assertEqual(response.status_code, 200)
#         self.assertIn(b"Weather data for San Francisco", response.data)

#     def test_weather_forecast_endpoint(self):
#         response = self.app.get('/weather/San Francisco/1')
#         self.assertEqual(response.status_code, 200)
#         # Add more assertions to check the forecast data

#     def test_add_city(self):
#         data = {
#             'city': 'Chicago',
#             'current': {'temperature': 18, 'weather': 'Partly Cloudy'},
#             'forecast': [
#                 {'temperature': 19, 'weather': 'Partly Cloudy'},
#                 {'temperature': 20, 'weather': 'Clear'},
#                 # Add more forecast entries for future days
#             ]
#         }
#         response = self.app.post('/weather/', data=json.dumps(data), content_type='application/json')
#         self.assertEqual(response.status_code, 201)
#         self.assertIn(b"City added successfully", response.data)

#     def test_add_invalid_city(self):
#         data = {
#             'current': {'temperature': 18, 'weather': 'Partly Cloudy'},
#             'forecast': [
#                 {'temperature': 19, 'weather': 'Partly Cloudy'},
#                 {'temperature': 20, 'weather': 'Clear'},
#             ]
#         }
#         response = self.app.post('/weather/', data=json.dumps(data), content_type='application/json')
#         self.assertEqual(response.status_code, 400)

#     def test_add_invalid_weather_data(self):
#         data = {
#             'city': 'Chicago',
#             'current': {'temperature': 18, 'weather': 'Partly Cloudy'},
#         }
#         response = self.app.post('/weather/', data=json.dumps(data), content_type='application/json')
#         self.assertEqual(response.status_code, 400)

# if __name__ == '__main__':
#     unittest.main()

# # import unittest
# # from app import app

# # class WeatherAppTestCase(unittest.TestCase):

# #     def setUp(self):
# #         self.app = app.test_client()

# #     def test_weather_endpoint(self):
# #         response = self.app.get('/weather/San Francisco')
# #         self.assertEqual(response.status_code, 200)
# #         self.assertIn(b"Weather data for San Francisco", response.data)

# #     def test_weather_forecast_endpoint(self):
# #         response = self.app.get('/weather/San Francisco/1')
# #         self.assertEqual(response.status_code, 200)
# #         # Add more assertions to check the forecast data

# #     def test_invalid_city(self):
# #         response = self.app.get('/weather/InvalidCity/1')
# #         self.assertEqual(response.status_code, 404)

# #     def test_invalid_day(self):
# #         response = self.app.get('/weather/San Francisco/-1')
# #         self.assertEqual(response.status_code, 400)

# # if __name__ == '__main__':
# #     unittest.main()


# # # import unittest
# # # from app import app

# # # tests/test_app.py
# # import unittest
# # from app import app

# # class WeatherAppTestCase(unittest.TestCase):

# #     def setUp(self):
# #         self.app = app.test_client()

# #     def test_weather_endpoint(self):
# #         response = self.app.get('/weather/San Francisco')
# #         self.assertEqual(response.status_code, 200)
# #         self.assertIn(b"Weather data for San Francisco", response.data)

# # if __name__ == '__main__':
# #     unittest.main()
