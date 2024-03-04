# Django-Learning

# Instructions
## Django
### Create a Django project
```
django-admin startproject PROJECT_NAME
```

### Add a new app to the Django project
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

### Create Admin user
```
python3 manage.py createsuperuser
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
### Add a description to your commit message
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
1. Make a branch with a clear name for the feature you want to add: `git checkout -b BRANCH_NAME`. If the branch already exists, then no need for the `-b` in the command.
1. Modify your changes on your local device.
1. When the modifications are finished: `git add *` to add all of the modified files.
1. Commit your work and write a clear message for your commit: `git commit -m "Your Message"`.
1. Push your work: `git push origin BRANCH_NAME`.
1. Go to the repo in GitHub, and add your commit as a pull request.
1. Go to Pull Requests and review your code.
1. If your changes got approved, merge them with the main branch.
1. Delete the used branch once the feature you're working on is finished.

### Common .gitignore content
```
**/__pycache__
**/migrations
.vscode
*.sqlite3
```

## Naming Conventions
### Variables
- Use lowercase letters with words separated by underscores.
- Nouns are preferred.
- Boolean variables are preferred to start with `is` like `is_valid` 

### Functions and Methods 
- Use lowercase letters with words separated by underscores.
- Verbs are preferred.
- Boolean Functions and Methods are preferred to start with `is` like `is_valid()` 
```python
def my_function():
    pass
```

### Classes
- Class names should follow the UpperCaseCamelCase convention.
- Nouns are preferred.
```python
class MyClass:
    pass
```

### Constants
- Use uppercase letters with words separated by underscores. Constants are typically used for variables that should not be changed.
```python
MAX_VALUE = 100
```

### Packages
- Should also be lowercase with words separated by underscores.
```python
from my_package import my_module
```

### Private Variables and Methods
Prefix names with a single leading underscore to indicate that they are intended for internal use.
```python
_internal_variable = 5

def _internal_function():
    pass
```

### Dunder (Double Underscore) Methods and Attributes: 
- Use double underscores for special methods and attributes.
```python
class MyClass:
    def __init__(self):
      pass
    def __str__(self):
      pass
```

### Files 
- Should also be lowercase with words separated by underscores.

### Django
- Project Name: The name of the Django project should be descriptive and follow Python's variable naming conventions (lowercase with underscores) e.g. `my_django_project/`.
- Application Names: Django applications should also follow Python's variable naming conventions.
- Database Models: like classes, CamelCase.
- Views: like function.
- Templates: Template files should be named with lowercase and may include underscores.
              
              my_app/
              └── templates/
                  └── my_app/
                      └── my_template.html

### Mysql with Django
### Connect MySQL DB
1- In MySQL Client, create a database.

2- In the `.env` file, add the 3 variables: DATABASE_NAME with the database name created in point 1, DATABASE_USER, and DATABASE_PASS. 

3- In `settings.py` file, change the `DATABASES` variable to the following:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASS'),
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
