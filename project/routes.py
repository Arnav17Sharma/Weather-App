from flask import Blueprint, render_template, url_for, request
import requests
from .data import give_me
from .types import type


main = Blueprint('main', __name__)


@main.route('/', methods=['POST', 'GET'])
def index():
    types = type()
    print("YOOO")
    data = {
        'name': '-',
        'coor': '-',
        'main_weather_type': '-',
        'current_temp': '-',
        'min_temp': '-',
        'max_temp': '-',
        'pressure': '-',
        'humidity': '-',
        'visibility': '-',
        'wind': '-',
        'dt': '-',
        'country': '-',
        'sun_time': '-',
        'timezone': '-'
    }
    message = ''
    no_data = False
    if request.method == "POST":
        if not give_me(request.form.get('query')):
            no_data = True
        else:
            data = give_me(request.form.get('query'))
            message = "Results"
    if request.method == "GET":
        message = "Search any city or no Results found!"

    return render_template('index.html', data=data, message=message, types=types)
