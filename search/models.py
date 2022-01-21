from django.db import models

# Create your models here.

class Search(models.Model):
  user = models.ForeignKey('users.Users', on_delete= models.CASCADE, related_name= 'search')
  user_name = models.TextField()

  class Meta:
    db_table = 'search'