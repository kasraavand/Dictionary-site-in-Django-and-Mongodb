from django.db import models
from djangotoolbox.fields import ListField


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    tags = ListField()
    comments = ListField()


# Create your models here.
