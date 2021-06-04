from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length =100)
    content = models.CharField(max_length=100)
    # author_director_or_draw = models.CharField(max_length=100)
    # genre = models.CharField(max_length=100)
    # runtime = models.IntegerField()
    # year_made = models.DateField(auto_now=False)
    # status = models.CharField(choices = ['Recommended','Downloaded', 'Completed', 'Abandoned', 'Completed'])
    # synopsis = models.TextField()
    # review = models.TextField()
    # rating = models.CharField()
    # recommend = models.CharField(choices =['Yes','No'])
    
    date_posted = models.DateTimeField( default = timezone.now)
    # date posted auto, but you can't change the posted date
    # date_posted = models.DateTimeField( auto_now_add = True)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    # on_delete = CASCADE deletes all posts by a user if the user is deleted

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    