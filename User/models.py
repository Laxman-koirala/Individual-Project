from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    following = models.ManyToManyField(User,related_name='following',blank = True)
    bio = models.TextField(default='no bio submitted..')
    photo = models.ImageField(upload_to= 'Profile_pic',null = True, blank = True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def profiles_posts(self):
        return self.post_set.all()

    def __str__(self):
        return str(self.user.username)

    class Meta:
        ordering = ('-created',)
