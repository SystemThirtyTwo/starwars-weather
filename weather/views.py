import requests, json
import os
from django.shortcuts import render
from dotenv import load_dotenv
from .forms import LocationForm


load_dotenv()

# Create your views here.
def index(request):
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            location = form.cleaned_data["location"].lower()

            return render(request, "weather/index.html", {
            "temp": get_api_response(),
            "form": LocationForm()
        })

        else:
            raise 404
    else:
        return render(request, "weather/index.html", {
            "temp": get_api_response(),
            "form": LocationForm()
        })

def get_api_response():
    access_key = os.getenv("KEY")

    url = f"https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={access_key}"

    
    """response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return "Failure to get data."""