DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'westagram',
        'USER': 'root',
        'PASSWORD': '19950807',
        'HOST': '127.0.0.1',
        'PORT': '3306',
     	'OPTIONS': {'charset': 'utf8mb4'}
    }
}
        
SECRET_KEY = 'django-insecure-_n1t%^&)+5*5!6yb181#1!_8bl^ersu6pgplgnpq3fdt8r!ce@'

ALGORITHM ='HS256'
