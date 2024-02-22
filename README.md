# Django-Learning

# Instructions
## Django
### Create a Django project
```
django-admin startproject PROJECT_NAME
```

### Add a new app to Django project
```
python3 manage.py startapp APP_NAME
```

### Run Django server
```
python3 manage.py runserver
```

### Make database migrations
```
python3 manage.py makemigrations APP_NAME
```

### Migrate database
```
python3 manage.py migrate
```

### Enable admin for an application
1. Create admin user: `python3 manage.py createsuperuser`
1. In `admin.py` file, register the models you have in `models.py` file for each app as follows:
```
from .models import MODEL1, MODEL2

admin.site.register(MODEL1)
admin.site.register(MODEL2)
```

### Steps to do after starting a new app
1. Add the app name to `INSTALLED_APPS` list in `settings.py` file.
1. Create `urls.py` file inside the new app and add `urlpatterns` list containing the paths for your app. Also, add the variable `app_name = "APP_NAME"` to avoid name collisions.
1. In the main `urls.py` file for the project, include the urls for the new app. (e.g `path('APP_NAME/', include('APP_NAME.urls')),`)
1. If the app will have html content, create `templates/APP_NAME` folder to add the html files in it.
1. Also, you can create `static/APP_NAME` for static files such as `css` and `js` files and images.

## Git
### Add description to your commit message
```
git commit -m "Commit message" -m "Commit description line #1" -m "Commit description line #2"
```

### Simple version
1. `git clone LINK`
2. `git status` to view your git status.
3. `git add File` to add a file or `git add *` to add all files.
4. `git commit -m ""` to commit your messages.
5. `git push origin main` to push your commits to Github.
6. `git pull origin main` to pull any changes from GitHub to your local workspace. 

### Upload your work to your Repo
1. `git clone LINK`
1. Make a branch with a clear name for the feature you want to add: `git checkout -b BRANCH_NAME`. If the branch is already exist, then no need for the `-b` in the command.
1. Modify your changes on your local device.
1. When the modifications are finished: `git add *` to add all of the modified files.
1. Commit your work and write a clear message for your commit: `git commit -m "Your Message"`.
1. Push your work: `git push origin BRANCH_NAME`.
1. Go to the repo in GitHub, and add your commit as a pull request.
1. Go to Pull Requests and review your code.
1. If your changes got approved then merge it to the main branch.
1. Delete the used branch once the feature you're working on is finished.

### Common .gitignore content
```
**/__pycache__
**/migrations
.vscode
*.sqlite3
```
