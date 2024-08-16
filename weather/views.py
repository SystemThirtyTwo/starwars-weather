import requests
import os
from django.shortcuts import render
from dotenv import load_dotenv


load_dotenv()

# Create your views here.
def index(request):
    access_key = os.getenv("KEY")
    return render(request, "weather/index.html", {
        "temp": 1
    })