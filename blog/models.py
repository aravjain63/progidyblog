from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone, dateformat
from django.contrib.auth.models import User

class Post(models.Model):
    author_name = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='post/image', null = True, blank = True)
    
    class Meta:
        ordering = ['-published_date']

    #bookmark = models.BooleanField(default=False)
    #number_of_likes = models.IntergerField(default = 0)
    #email = models.models.CharField(_("enter your email"), max_length=50)
    def __str__(self):
        return self.title        
    def publish(self):
        self.published_date = timezone.now
        self.save()
    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs) 


       

# Create your models here.
