from flask import Blueprint, render_template, url_for, request
import requests
from .data import give_me
from .types import type


main = Blueprint('main', __name__)


@main.route('/', methods=['POST', 'GET'])
def index():
    types = type()
    print("YOOO")
    data = []
    message = ''
    no_data = False
    if request.method == "POST":
        if not give_me(request.form.get('query')):
            no_data = True
        else:
            data = give_me(request.form.get('query'))
            message = "Results"
    if no_data:
        message = "No Results found!"

    return render_template('index.html', data=data, message=message, types=types)
