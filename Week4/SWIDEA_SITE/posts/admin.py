from django.contrib import admin
from .models import DevTool, Post

# Register your models here.
admin.site.register(Post)
admin.site.register(DevTool)