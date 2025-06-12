import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk

API_KEY = "8b1ffcc1b5880b7e1a2eeb716fd48008"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Enter a city name.")
        return

    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        city_label.config(text=f"Weather in {city}")
        temp_label.config(text=f"Temperature: {data['main']['temp']}°C")
        hum_label.config(text=f"Humidity: {data['main']['humidity']}%")
        cond_label.config(text=f"Condition: {data['weather'][0]['description']}")
    else:
        messagebox.showerror("Error", "Could not retrieve data.")

# GUI setup
root = tk.Tk()
root.title("Weather App")
root.geometry("300x250")

city_entry = tk.Entry(root)
city_entry.pack(pady=10)

get_btn = tk.Button(root, text="Get Weather", command=get_weather)
get_btn.pack()

city_label = tk.Label(root, text="", font=("Helvetica", 14))
city_label.pack(pady=5)

temp_label = tk.Label(root, text="")
temp_label.pack()

hum_label = tk.Label(root, text="")
hum_label.pack()

cond_label = tk.Label(root, text="")
cond_label.pack()

root.mainloop()
