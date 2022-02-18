import requests

api_key = ""
base_url = "http://api.openweathermap.org/data/2.5/weather"

ip = input("Please enter a city name or cities name with space: ").strip().split()

for city in ip:
    request_url = f"{base_url}?q={city}&appid={api_key}"

    response = requests.get(request_url)

    if response.status_code == 200:
        response_json = response.json()
        weather = response_json['weather'][0]['description'].title()
        temp = round((response_json['main']['temp'] - 273), 2)
        print(f"{response_json['name']} -- Current Temperature is {temp}°C & Weather is {weather}")
    else:
        print(f"Invalid city name  {city}")