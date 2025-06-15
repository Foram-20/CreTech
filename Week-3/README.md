# 🌦️ Weather Info App

A simple command-line weather app built with **Python** using the **OpenWeatherMap API**. It fetches and displays real-time weather details such as temperature, humidity, wind speed, and conditions for any city you input.

---

## 📌 Features

- Fetches **current weather data** from OpenWeatherMap  
- Displays user-friendly output with temperature, humidity, and wind speed  
- Handles API errors and invalid city names  
- Runs completely in the terminal (no GUI required)  

---

## 🧠 Project Architecture

1. **Choose a weather API provider** (e.g., OpenWeatherMap)  
2. **Implement methods** for fetching weather data (e.g., current weather)  
3. **Parse the API response** and extract key fields: temperature, humidity, wind speed, etc.  
4. **Display the weather** in a clean, user-friendly format in the terminal  
5. **Test the API integration** with sample inputs and handle errors gracefully  

---

## 🛠️ Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/weatherapi.git
cd weatherapi

````

### Step 2: Install Required Library

```bash
pip install requests
```

---

## 🚀 How to Run

```bash
python weatherapi.py
```

You’ll see:

```text
=== 🌦️ Weather Info App ===
Enter city name (or type 'exit' to quit):
```

---

## 🧪 Sample Output

```text
🌤️ Weather in Ahmedabad:
📍 Description: Broken Clouds
🌡️ Temperature: 37.47 °C
💧 Humidity: 36%
💨 Wind Speed: 3.37 m/s
```

---

## 🔑 API Key Setup

* Go to [OpenWeatherMap](https://openweathermap.org/api)
* Sign up and generate your **free API key**
* Replace the `api_key` value inside `weather_app.py`:

```python
api_key = "YOUR_API_KEY_HERE"
```

✅ This project uses a **hardcoded API key** for simplicity. For production use, store it in `.env` or environment variables.

---

## 📂 File Structure

```
weather-info-app/
│
├── weatherapi.py       # Main Python script
├── README.md            # Project documentation
```

---

## 📄 License

This project is licensed under the MIT License.

---
