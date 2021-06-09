import requests

url = 'http://localhost:8000/api/capitals/'  # Полный адрес эндпоинта
response = requests.get(url)  # Делаем GET-запрос
# Поскольку данные пришли в формате json, переведем их в python
response_on_python = response.json()
# Запишем полученные данные в файл capitals.txt
with open('capitals.txt', 'w') as file:
    for capital in response_on_python:
        file.write(
            f"The population of {capital['capital_city']} is "
            f"{capital['capital_population']}, "
            f"author - {capital['author']}\n"
        )
