from django.db import models
from django.urls import reverse

class Comic(models.Model):
    title = models.CharField(max_length=30)
    series = models.IntegerField()
    issuenumber = models.IntegerField()
    summary = models.TextField(max_length=200)
    releasedate = models.DateField()
    publisher = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'comic_id': self.id})


