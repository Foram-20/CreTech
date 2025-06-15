import requests

def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                "city": city_name.title(),
                "description": data['weather'][0]['description'].title(),
                "temperature": data['main']['temp'],
                "humidity": data['main']['humidity'],
                "wind_speed": data['wind']['speed']
            }
            return weather_data
        else:
            return None
    except requests.exceptions.RequestException as e:
        print("⚠️ Error:", e)
        return None

def display_weather(data):
    if data:
        print(f"\n🌤️ Weather in {data['city']}:")
        print(f"📍 Description: {data['description']}")
        print(f"🌡️ Temperature: {data['temperature']} °C")
        print(f"💧 Humidity: {data['humidity']}%")
        print(f"💨 Wind Speed: {data['wind_speed']} m/s\n")
    else:
        print("❌ City not found or API error.")

def main():
    print("=== 🌦️ Weather Info App ===")
    api_key = "caea4b9f49c2dfae634017e1740e9882"  # ✅ Your valid OpenWeatherMap API key

    while True:
        city = input("Enter city name (or type 'exit' to quit): ")
        if city.lower() == "exit":
            print("👋 Goodbye!")
            break
        weather_data = get_weather(city, api_key)
        display_weather(weather_data)

if __name__ == "__main__":
    main()
