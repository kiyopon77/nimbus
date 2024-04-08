# app.py 

# Import required modules
import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap

# function to get weather info from owm api
def get_weather(city):
    API_key = "020814103a2c3e707aeb11f347ed10f2"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("Error", "City not found")
        return None

    # parse the response json to get weather info
    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    temperature = weather['main']['temp'] - 273.15
    description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']

    #get the icon url and return all the weather info
    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url, temperature, description, city, country)

# funtion to search weatherfor city
def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return
    
    # if the city is found, unpack the weather info
    icon_url, temperature, description, city, country = result
    location_label.configure(text = f"{city}, {country}")

    # get the weather icon image from the URL and update the icon label
    image = Image.open(requests.get(icon_url, stream = True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image = icon)
    icon_label.image = icon

    # update the temp and weather labels
    temperature_label.configure(text = f"Temperature: {temperature:.2f}°C")
    description_label.configure(text = f"Description: {description}")

root = ttkbootstrap.Window(themename = "morph")
root.title("Nimbus")
root.geometry("400x400")

# Entry widget -> to enter city 
city_entry = ttkbootstrap.Entry(root, font = "Bahnschrift, 16")
city_entry.pack(pady = 10)

# Button widget -> to search weather
search_button = ttkbootstrap.Button(root, text = "Search", command = search, bootstyle = "warning")
search_button.pack(pady = 10)

# Label widget -> to show country/city
location_label = tk.Label(root, font = "Bahnschrift, 25")
location_label.pack(pady = 20)

# Label widget -> to show the weather icon
icon_label = tk.Label(root)
icon_label.pack()

# Label widget -> to show the temp
temperature_label = tk.Label(root, font = "Bahnschrift, 14")
temperature_label.pack()

# Label widget -> to show weather description
description_label = tk.Label(root, font = "Bahnschrift, 17")
description_label.pack()

root.mainloop()
