from django.contrib import admin

from .models import Categories,Post

# Register your models here.
admin.site.register(Post)
admin.site.register(Categories)
