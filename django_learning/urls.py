from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("app_navigator.urls")),
    path("hello/", include("hello.urls")),
    path("birthday/", include("birthday.urls")),
    path("todo/", include("todo.urls")),
    path("flights/", include("flights.urls")),
    path("users/", include("users.urls")),
    path("admin/", admin.site.urls),
]
