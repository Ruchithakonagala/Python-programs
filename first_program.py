import tkinter as tk
from tkinter import messagebox
import requests

# Function to get weather data
def get_weather():
    city = city_entry.get()
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # Construct the complete API URL
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    
    # Fetch the data
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        temperature = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        weather_description = weather["description"]
        
        # Display the results
        result_text = (f"City: {city}\n"
                       f"Temperature: {temperature}°C\n"
                       f"Pressure: {pressure} hPa\n"
                       f"Humidity: {humidity}%\n"
                       f"Description: {weather_description.capitalize()}")
        result_label.config(text=result_text)
    else:
        messagebox.showerror("Error", "City not found!")

# Create the main window
root = tk.Tk()
root.title("Real-Time Weather Dashboard")

# Create and place the widgets
city_label = tk.Label(root, text="Enter City Name:")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack()

result_label = tk.Label(root, text="", justify=tk.LEFT)
result_label.pack()

# Run the application
root.mainloop()