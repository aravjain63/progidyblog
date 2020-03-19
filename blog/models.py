from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User

class Post(models.Model):
    author_name = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)
    #number_of_likes = models.IntergerField(default = 0)
    #email = models.models.CharField(_("enter your email"), max_length=50)
    def __str__(self):
        return self.title
        
    def publish(self):
        self.published_date = timezone.now
        self.save()


 
        


#Class Email(models.Model):
    #author_id = models.ForeignKey(Post,on_delete=models.CASCADE)



       

# Create your models here.
