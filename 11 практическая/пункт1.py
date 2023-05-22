import json
from urllib.request import Request, urlopen
from datetime import datetime

class Weather:
    def __init__(self, data):
        self.temp = data['main']['temp']
        self.description = data['weather'][0]['description']
        self.humidity = data['main']['humidity']
        self.wind_speed = data['wind']['speed']
        self.pressure = data['main']['pressure']
        self.city_name = data['name']

    def __str__(self):
        currentTime = datetime.now().strftime("%H:%M:%S")

        return f"""[{currentTime}] Запрос погоды в городе: {self.city_name}
Температура: {self.temp} °C, {self.description}
Влажность воздуха: {self.humidity}%
Скорость ветра: {self.wind_speed} м/с
Атмосферное давление: {self.pressure} мм рт. ст\n"""
    
app_id = 'c341e34f9b7c327502cde34aa7817c5f'
url_template = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&lang=ru&appid={}'

city_name = input('Введите название гороода: ')

request = Request(url_template.format(city_name, app_id))
with urlopen(request) as response:
    content = response.read().decode('utf-8')
    data = json.loads(content)

weather = Weather(data)

print(weather.__str__())
with open('./weather.txt', 'a', encoding="utf-8") as log:
    log.write(weather.__str__())