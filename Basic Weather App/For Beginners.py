import requests

API_KEY = "8b1ffcc1b5880b7e1a2eeb716fd48008"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    response = requests.get(BASE_URL, params=params)
    print("Request URL:", response.url)
    print("Status Code:", response.status_code)

    if response.status_code == 200:
        data = response.json()
        print(f"\nWeather in {city}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Condition: {data['weather'][0]['description']}")
    else:
        print("Error fetching weather data. Check your city name or API key.")
        print("Response:", response.text)

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)