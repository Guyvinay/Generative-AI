# app.py (update the app.py file)
from flask import Flask, jsonify, request

app = Flask(__name__)

weather_data = {
    'San Francisco': {
        'current': {'temperature': 14, 'weather': 'Cloudy'},
        'forecast': [
            {'temperature': 15, 'weather': 'Cloudy'},
            {'temperature': 16, 'weather': 'Partly Cloudy'},
            # Add more forecast entries for future days
        ]
    },
    'New York': {
        'current': {'temperature': 20, 'weather': 'Sunny'},
        'forecast': [
            {'temperature': 22, 'weather': 'Sunny'},
            {'temperature': 23, 'weather': 'Clear'},
            # Add more forecast entries for future days
        ]
    },
    # Add data for other cities
}

@app.route('/weather/<string:city>/')
def get_weather(city):
    if city in weather_data:
        return jsonify(weather_data[city]['current'])
    else:
        return "City not found", 404

@app.route('/weather/<string:city>/<int:days_in_future>/')
def get_weather_forecast(city, days_in_future):
    if city in weather_data:
        if 0 <= days_in_future < len(weather_data[city]['forecast']):
            return jsonify(weather_data[city]['forecast'][days_in_future])
        else:
            return "Invalid day", 400
    else:
        return "City not found", 404


# from flask import Flask, jsonify

# app = Flask(__name__)

# weather_data = {
#     'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
#     'New York': {'temperature': 20, 'weather': 'Sunny'},
#     'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
#     'Seattle': {'temperature': 10, 'weather': 'Rainy'},
#     'Austin': {'temperature': 32, 'weather': 'Hot'},
# }

# @app.route('/weather/<string:city>/')
# def get_weather(city):
#     if city in weather_data:
#         return jsonify(weather_data[city])
#     else:
#         return "City not found", 404




# # @app.route('/weather/<string:city>/')
# # def get_weather(city):
# #     return f"Weather data for {city}"


if __name__==('__main__'):
    app.run(debug=True)