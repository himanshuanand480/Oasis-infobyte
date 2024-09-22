#first we need to install module requests 
import requests
def weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key + "&units=metric"
    response = requests.get(complete_url)
    
    if response.status_code == 200:
        data = response.json()
        # Extract weather information
        main = data['main']
        temperature = main['temp']
        humidity = main['humidity']
        weather_desc = data['weather'][0]['description']
        # Display weather details
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather_desc.capitalize()}")
    else:
        print("City not found.")
#enter your api from  google
api_key = "f1b725079d5dde0f9dbf46a3dee13ca3"
city_name = input("Enter city name: ")
weather(city_name, api_key)
