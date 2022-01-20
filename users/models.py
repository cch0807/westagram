from django.db import models

class Users(models.Model):
  name         = models.CharField(max_length=30)
  email        = models.CharField(max_length=100, unique=True) 
  password     = models.CharField(max_length=200)
  phone_number = models.CharField(max_length=30, unique=True)
  create_at    = models.DateTimeField(auto_now_add=True)
  modified_at  = models.DateTimeField(auto_now=True)

  class Meta:
    db_table   = 'users'
