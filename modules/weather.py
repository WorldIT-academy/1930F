import requests
from .json_folder.write_json import *

API_KEY = '5805fbd4ff0e0c4ebcf6e12c051e3507'
def update_weather(city_name):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric&lang=ua'
    response = requests.get(url)

    if response.status_code == 200:
        print("sucsessful")
        # Метод json() преображает полученные данные в json формат
        data = response.json()
        write(data, "weather_data.json")
    else:
        print("error")
