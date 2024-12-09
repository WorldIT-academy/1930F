import requests
import json
# requests - нужен для получения данных по ссылке 

API_KEY = "336633f9d31fd19a2d94570ca76d354f"
city_name = 'London'
# Создаем ссылку
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'
# Получаем данные
response = requests.get(url)
# 200 - Успешно полученные данные
# Любой другой код ошибка
if response.status_code == 200:
    print(response)

    data = response.json()
    # print(json.dumps(data, indent = 4))
    temp = data["main"]["temp"]
    print(int(temp - 273.15))