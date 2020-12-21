import requests
import json


def give_me(city_name):
    print("DATA")
    API_KEY = '701726f03e98fea267e17f9e15b584f0'
    link = 'https://api.openweathermap.org/data/2.5/weather?q='+city_name+'&appid='+API_KEY
    r = requests.get(link).json()
    try:
        sample = {
            'name': r['name'],
            'coor': [r['coord']['lon'], r['coord']['lat']],
            'main_weather_type': r['weather'][0]['main'],
            'current_temp': r['main']['temp'],
            'min_temp': r['main']['temp_min'],
            'max_temp': r['main']['temp_max'],
            'pressure': r['main']['pressure'],
            'humidity': r['main']['humidity'],
            'visibility': r['visibility'],
            'wind': [r['wind']['speed'], r['wind']['deg']],
            'dt': r['dt'],
            'country': r['sys']['country'],
            'sun_time': [r['sys']['sunrise'], r['sys']['sunset']],
            'timezone': r['timezone']
        }
    except:
        return False
    return sample


# print(give_me('bhilai'))
# {'coord': {'lon': 81.43, 'lat': 21.22}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'base': 'stations', 'main': {'temp': 300.55, 'feels_like': 299.57, 'temp_min': 300.55, 'temp_max': 300.55, 'pressure': 1013, 'humidity': 30, 'sea_level': 1013, 'grnd_level': 980}, 'visibility': 10000, 'wind': {'speed': 0.83, 'deg': 291}, 'clouds': {'all': 0}, 'dt': 1608285206, 'sys': {'country': 'IN', 'sunrise': 1608253543, 'sunset': 1608292573}, 'timezone': 19800, 'id': 1275971, 'name': 'Bhilai', 'cod': 200}
