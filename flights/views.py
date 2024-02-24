from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Flight, Passenger

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights" : Flight.objects.all()
    })

def single_flight(request, flight_id):
    try:
        flight = Flight.objects.get(pk = flight_id)
        return render(request, "flights/single_flight.html", {
            "flight" : flight,
            "passengers" : flight.passengers.all(),
            "non_passengers" : Passenger.objects.exclude(flights = flight).all(),
        })
    except Flight.DoesNotExist:
        return render(request, "flights/error.html", {
            "message" : "No flight with the given id"
        })

def book(request, flight_id):
    if request.method == 'POST':
        passenger_id = request.POST['passenger'] 
        passenger = Passenger.objects.get(pk = passenger_id)
        flight = Flight.objects.get(pk = flight_id)
        passenger.flights.add(flight)

        return HttpResponseRedirect(reverse('flights:single_flight', args = (flight_id,)))