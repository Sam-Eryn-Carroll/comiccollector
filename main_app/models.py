from django.db import models
from django.urls import reverse

RATING = (
    (0, 'Zero'),
    (1, 'One'),
    (2, 'Two'),
    (3, 'Three'),
    (4, 'Four'),
    (5, 'Five')
)

class Character(models.Model):
    name = models.CharField(max_length=50)
    power = models.CharField(max_length=300)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('characters_detail', kwargs={'pk': self.id})

class Comic(models.Model):
    title = models.CharField(max_length=30)
    series = models.IntegerField()
    issuenumber = models.IntegerField()
    summary = models.TextField(max_length=200)
    releasedate = models.DateField()
    publisher = models.CharField(max_length=20)
    characters = models.ManyToManyField(Character)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'comic_id': self.id})

class Review(models.Model):
    date = models.DateField('review date')
    rating = models.IntegerField(choices=RATING, default=RATING[0][0])
    review_text = models.TextField(max_length=100)

    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_rating_display()} on {self.date}"

    class Meta:
        ordering = ['date']


