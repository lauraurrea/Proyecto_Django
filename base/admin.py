from django.contrib import admin
from .models import Post, Comment, Amigos, Soporte, Megusta

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Amigos)
admin.site.register(Soporte)
admin.site.register(Megusta)