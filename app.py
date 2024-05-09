# app.py
import requests

# OpenWeatherMap API key
api_key = '2a22ee2d87b09d70b65a25d5661f2f00'

city = 'Tokyo'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)

