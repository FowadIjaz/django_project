from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length =100)
    content = models.TextField()
    date_posted = models.DateTimeField( default = timezone.now)
    # date_posted = models.DateTimeField( auto_now_add = True)
    # date posted auto, but you can't change the posted date
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    # on_delete = CASCADE deletes all posts by a user if the user is deleted

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    