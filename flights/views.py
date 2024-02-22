from django.shortcuts import render

from .models import Flight

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights" : Flight.objects.all()
    })

def single_flight(request, flight_id):
    try:
        flight = Flight.objects.get(pk = flight_id)
        return render(request, "flights/single_flight.html", {
            "flight" : flight
        })
    except:
        return render(request, "flights/error.html", {
            "message" : "No flight with the given id"
        })
