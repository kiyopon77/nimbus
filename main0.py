# app.py
import requests

# OpenWeatherMap API key
api_key = 'Your_API_Key'

city = 'Tokyo'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)

