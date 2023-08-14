from django.shortcuts import render
from django.http import HttpResponse
from .models import WeatherMeasurement as wm
import json

# Create your views here.
def index(request):
    data = wm.objects 
    context = {
        'data' : data,
    }
    return render(request, 'weather_data/index.html', context)

def liveData(request):
    db_data = wm.objects.latest('created')
    data = json.dumps(
            {
                "ambient_temperature":str(db_data.ambient_temperature),
                #"ground_temperature":str(db_data.ground_temperature),
                #"air_quality":str(db_data.air_quality),
                "air_pressure":str(db_data.air_pressure),
                "humidity":str(db_data.humidity),
                "wind_direction":str(db_data.wind_direction),
                "wind_speed":str(db_data.wind_speed),
                "wind_gust_speed":str(db_data.wind_gust_speed),
                "rainfall":str(db_data.rainfall)
            })
    return HttpResponse(data)
