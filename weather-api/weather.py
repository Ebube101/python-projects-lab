import requests

API_KEY = ""
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        condition = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        weather_info = f"Weather in {city}: Temperature: {temperature}°C | Condition: {condition} | Humidity: {humidity}%"
        print(weather_info)
        return weather_info  # Always return a valid string
    else:
        error_message = f"Error: Unable to fetch weather data for {city}. Please check the city name."
        print(error_message)
        return error_message  # Return an error message instead of None

# Accept user input for multiple cities
cities = input("Enter city names (comma-separated): ").split(",")
cities = [city.strip() for city in cities]

# Open log file in append mode
with open("weather_log.txt", "a") as log_file:
    for city in cities:
        weather_info = get_weather(city)
        log_file.write(weather_info + "\n")  # This will no longer cause a TypeError

print("\nWeather data has been logged successfully.")
