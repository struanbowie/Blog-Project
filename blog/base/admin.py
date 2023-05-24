from django.contrib import admin

# Register your models here.

from .models import Desk, Topic, Post

admin.site.register(Desk)
admin.site.register(Topic)
admin.site.register(Post)