## Screenshots:-

### Home Page

![Screenshot_2021-02-01 Real Estate](https://user-images.githubusercontent.com/57964315/106482567-c6251f80-64d7-11eb-8392-53b6c7348afe.png)

### All Listings Page
![Screenshot_2021-02-01 Featured Listings](https://user-images.githubusercontent.com/57964315/106483131-667b4400-64d8-11eb-9003-db488c3f82cd.png)


### Single Listing Page
![Screenshot_2021-02-01 Freshly Built Modern Villa](https://user-images.githubusercontent.com/57964315/106483241-81e64f00-64d8-11eb-9d86-f498f913c848.png)

### User Dashboard
![Screenshot_2021-02-01 Dashboard Abdullah](https://user-images.githubusercontent.com/57964315/106483590-e4d7e600-64d8-11eb-9a21-940abd2cec43.png)




## Creating a virtual environment

We need to create a virtual env for our app to run in: [More Here](https://docs.python.org/3/library/venv.html)
Run this command in your project folder:

```
virtualenv venv
```

### Activate the virtualenv

```
# Mac/Linux
source ./venv/bin/activate

# Windows
venv\Scripts\activate.bat - May need to add full path (c:\users\....venv\Scripts\activate.bat)
```

### Install all packages

```
pip install -r requirements.txt
```

### Migrate Your Database
Go to your project folder in open terminal also activate your virtualenv then run this command
```
py manage.py makemigrations
py manage.py migrate
py manage.py createsuperuser
```

### Install Django

```
pip install django
```


### Run Server (http://127.0.0.1:8000) CTRL+C to stop

```
python manage.py runserver
```

### For Email setup
Go to settings.py in bottom, there you can see:
```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = '' # Your Email Address
EMAIL_HOST_PASSWORD = '' # Your Email password
EMAIL_USE_SSL = False
```

Make sure your gmail account has been turn on Less secure app access:

https://myaccount.google.com/u/1/lesssecureapps?rapt=AEjHL4NSQFabNvSD8Jb51XLg1zDDBQXmf1RZCFU4QkFuiZmclvrZmyOYAuSgfjN6tjU1gJx_GjDunU4aWx_XFFbprJowVm4KMA


