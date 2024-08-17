import requests
import os
import pycountry
from django.shortcuts import render
from dotenv import load_dotenv
from .forms import LocationForm

load_dotenv()

def index(request):
    # if a user inputs something into the location box
    if request.method == "POST":
        form = LocationForm(request.POST)
        
        if form.is_valid():
            #clean the data
            input_location = form.cleaned_data["location"].lower()
            location = api_handler(f"http://api.openweathermap.org/geo/1.0/direct?q={input_location}&limit=1&appid=")
            
            country = pycountry.countries.get(alpha_2=location[0]["country"])
            weather = api_handler(f"https://api.openweathermap.org/data/2.5/weather?lat={location[0]["lat"]}&lon={location[0]["lon"]}&appid=")
            
            temperature = round(weather["main"]["temp"] - 273.15)
            
            #return the data to the user
            return render(request, "weather/index.html", {
                "temp": temperature,
                "country": country.name,
                "form": LocationForm(),
                "planet": determine_planet(temperature)
        })
        else:
            raise 404
    else:
        return render(request, "weather/index.html", {
            "temp": None,
            "form": LocationForm()
        })

def api_handler(url):
    access_key = os.getenv("KEY")

    url_key = url+access_key
    response = requests.get(url_key)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return "Failure to get data."
    
def determine_planet(temperature):
    if temperature <= 0:
        return "hoth"
    elif temperature >= 20:
        return "endor"
    elif temperature >= 30:
        return "batuu"
    elif temperature >= 45:
        return "tatooine"
    else:
        return "endor"