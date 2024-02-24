from django.urls import path

from . import views

app_name = 'flights'
urlpatterns = [
    path("", views.index, name = "index"),
    path("<int:flight_id>", views.single_flight, name = "single_flight"),
    path("book/<int:flight_id>", views.book, name = "book"),
]