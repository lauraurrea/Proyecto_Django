from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    
    # def __str__(self):
    #     return self.title
    
class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

class Amigos(models.Model):
    user = models.ForeignKey(User, related_name='amigos', on_delete=models.CASCADE)
    follow= models.ForeignKey(User,related_name='amigo_de', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'follow']

class Soporte(models.Model):
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()

class Megusta(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)