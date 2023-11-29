import requests
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()
API_KEY = os.getenv('API_KEY')


def get_weather(country, city):
    resp = requests.get(
        f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city},{country}&days=1').json()
    error = resp.get("error")
    if error and error.get('code') == 1006:
        return None
    else:
        code = resp.get('current').get('condition').get('code')
        Icon = get_icon(code)
        weather = {
            'country': resp.get('location').get('country'),
            'city': resp.get('location').get('name'),
            'temperature': resp.get('current').get('temp_c'),
            'text': resp.get('current').get('condition').get('text'),
            'icon': Icon,
            'feelslike': resp.get('current').get('feelslike_c'),
            'dateAndTime': resp.get('location').get('localtime'),
        }
        return weather


def get_forecast(country, city):
    resp = requests.get(
        f'http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city},{country}&days=8').json()
    error = resp.get("error")
    if error and error.get('code') == 1006:
        return None
    forecast = resp.get('forecast').get('forecastday')
    for day in forecast:
        condition_code = day['day']['condition']['code']
        day['icon'] = get_icon(condition_code)
        date = day['date']
        day_name = ['Monday', 'Tuesday', 'Wednesday',
                    'Thursday', 'Friday', 'Saturday', 'Sunday']
        date = datetime.strptime(date, '%Y-%m-%d').strftime('%d-%m-%Y')
        tday = datetime.strptime(date, '%d-%m-%Y').weekday()
        Day = day_name[tday]
        day['Day'] = Day
    return forecast


def get_icon(code):
    if code == 1000:  # sunny
        icon = '/static/png/1000.png'
    elif code == 1003:  # partly sunny
        icon = '/static/png/1003.png'
    elif code in (1006, 1009):  # cloudy
        icon = '/static/png/1006.png'
    elif code in (1030, 1135, 1147):
        icon = '/static/png/1030.png'
    elif code in (1066, 1114, 1117, 1219, 1210, 1213, 1216, 1222, 1225, 1237, 1255, 1258,):
        icon = '/static/png/1066.png'
    elif code in (1069, 1183, 1063, 1072, 1150, 1153, 1168, 1171, 1180, 1183, 1186.1189, 1192, 1195, 1198, 1201, 1204, 1207, 1240, 1243, 1246, 1249, 1252, 1261, 1264):
        icon = '/static/png/1183.png'
    elif code in (1087, 1273, 1276, 1279, 1282):
        icon = '/static/png/1276.png'
    return icon
