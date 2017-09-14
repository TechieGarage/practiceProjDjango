from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User) # here we are not inheriting User model as it may lead to creation
                             # of multiple instances in database. so we simply create one-to-one relation
    # Additional field adding into user
    portfolio_site = models.URLField(blank=True) # Optional
    profile_pic = models.ImageField(upload_to='profile_pics' , blank=True) # profile_pics is subfolder of
                                                                           # media folder
    def __str__(self):
        return self.user.username
