import requests
from django.shortcuts import render


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&id=524901&APPID=f430bad4763e6508740bd70bb9d0e0b5'
    city = 'Odessa'

    r = requests.get(url.format(city)).json()
    city_weather = {
        'city': city,
        'temperature': round(((r['main']['temp']-32) * 5/9), 2),
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }
    print(city_weather)
    return render(request, 'weather/weather.html')
