from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("hello/", include("hello.urls")),
    path("birthday/", include("birthday.urls")),
    path("todo/", include("todo.urls")),
    path("flights/", include("flights.urls")),
    path("admin/", admin.site.urls),
]
