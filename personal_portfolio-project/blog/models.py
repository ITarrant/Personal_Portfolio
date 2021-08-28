from django.db import models
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)
    blog = models.TextField()