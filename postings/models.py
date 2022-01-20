from django.db import models

# Create your models here.
class Post(models.Model):
  user = models.ForeignKey('users.Users', on_delete=models.CASCADE, related_name='posts')
  create_at = models.DateTimeField(auto_now_add=True)
  image = models.URLField()
  post = models.TextField()

  class Meta:
    db_table= 'posts'

class Commit(models.Model):
  user = models.ForeignKey('users.Users', on_delete=models.CASCADE, related_name='comments')
  post= models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
  create_at = models.DateTimeField(auto_now_add=True)
  comment = models.TextField()

  class Meta:
    db_table = 'comments'