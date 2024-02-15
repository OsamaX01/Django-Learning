from django.shortcuts import render

import datetime

# Create your views here.
def index(requst):
    now = datetime.datetime.now()
    is_my_birthday = now.month == 12 and now.day == 31
    return render(requst, "birthday/index.html", {
        "is_my_birthday": is_my_birthday   
    })