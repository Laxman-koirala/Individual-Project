from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from User.models import Profile

# Create your models here.
class Categories(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return '%s'%(self.title)

class Post(models.Model):
    title = models.CharField(max_length = 50)
    overview = models.TextField()
    time_upload = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    Author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to= 'thumbnail', blank=True,null=True)
    categories = models.ManyToManyField(Categories, blank = True)
    view = models.IntegerField(default = 1)

    class Meta:
        ordering =['-time_upload']

    def __str__(self):
        return '%s'%(self.title)
