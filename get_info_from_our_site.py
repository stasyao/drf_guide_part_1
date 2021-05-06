import requests

url = 'http://localhost:8000/api/capitals/' # полный адрес эндпоинта
response = requests.get(url) # делаем GET-запрос
# поскольку данные пришли в формате json, переведем их в python
response_in_python = response.json()
# запишем полученные данные в файл capitals.txt
with open('capitals.txt', 'w') as file:
    for capital in response_in_python:
        file.write(f"The population of {capital['capital_city']} is {capital['capital_population']}\n")
