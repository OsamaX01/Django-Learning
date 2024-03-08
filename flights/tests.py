from django.test import Client, TestCase
from django.db.models import Max

from .models import Flight, Airport, Passenger

# Create your tests here.
class FlightTestCase(TestCase):

    def setUp(self):
        airport1 = Airport.objects.create(city = "A", code = 1)
        airport2 = Airport.objects.create(city = "B", code = 2)

        Flight.objects.create(origin = airport1, destination = airport2, duration = 100)
        Flight.objects.create(origin = airport1, destination = airport1, duration = 200)
        Flight.objects.create(origin = airport1, destination = airport2, duration = -100)

    def test_departures_count(self):
        departures = Airport.objects.get(code = 1).departures
        self.assertEqual(departures.count(), 3)

    def test_arrivals_count(self):
        arrivals = Airport.objects.get(code = 2).arrivals
        self.assertEqual(arrivals.count(), 2)

    def test_valid_flight(self):
        airport1 = Airport.objects.get(code = 1)
        airport2 = Airport.objects.get(code = 2)
        flight = Flight.objects.get(origin = airport1, destination = airport2, duration = 100)
        self.assertTrue(flight.is_valid_flight())

    def test_valid_flight_destination(self):
        airport1 = Airport.objects.get(code = 1)
        flight = Flight.objects.get(origin = airport1, destination = airport1, duration = 200)
        self.assertFalse(flight.is_valid_flight())

    def test_valid_flight_duration(self):
        airport1 = Airport.objects.get(code = 1)
        airport2 = Airport.objects.get(code = 2)
        flight = Flight.objects.get(origin = airport1, destination = airport2, duration = -100)
        self.assertFalse(flight.is_valid_flight())

    def get_status_code(self, url):
        client = Client()
        response = client.get(url)
        return response.status_code
    
    def get_context_attribute(self, url, attribute):
        client = Client()
        response = client.get(url)
        return response.context[attribute]
    
    def test_index(self):
        url = "/flights/"
        status_code = self.get_status_code(url)
        flights = self.get_context_attribute(url, "flights")

        self.assertEqual(status_code, 200)
        self.assertEqual(flights.count(), 3)

    def test_valid_single_flight(self):
        airport = Airport.objects.get(code=1)
        flight = Flight.objects.get(origin = airport, destination = airport)
        url = f"/flights/{flight.id}"
        status_code = self.get_status_code(url)

        self.assertEqual(status_code, 200)

    def test_invalid_single_flight(self):
        last_flight_id = Flight.objects.all().aggregate(Max("id"))["id__max"]
        url = f"/flights/{last_flight_id + 1}"
        status_code = self.get_status_code(url)

        #200 because invalid id should be redirected to error html page
        self.assertEqual(status_code, 200)