from django.shortcuts import render

from django_learning import settings

def filter_out_django_apps(apps):
    apps_result = [app for app in apps if 'django' not in app]
    apps_result.remove('app_navigator')
    return apps_result

def add_urls_to_app_names(apps):
    apps_result = []
    for app_name in apps:
        app_url = app_name + ":index"
        app = (app_name, app_url)
        apps_result.append(app)

    return apps_result

# Create your views here.
def index(request):
    apps = settings.INSTALLED_APPS
    apps = filter_out_django_apps(apps)    
    apps = add_urls_to_app_names(apps)
    return render(request, "app_navigator/index.html", {
        "apps" : apps
    })