from django.urls import path

from . import views

app_name = "app_navigator"
urlpatterns = [
    path("", views.index, name = "index"),    
]