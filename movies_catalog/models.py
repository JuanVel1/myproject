from django.db import models

# Create your models here.
from django.urls import reverse


class Director(models.Model):
    name = models.CharField(max_length=64, help_text='Pon el nombre del director')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('director-detail', args=[str(self.id)])


class Movie(models.Model):
    title = models.CharField(max_length=32)
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    year = models.FloatField(max_length=32)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie-detail', args=[str(self.id)])


class Meta(models.Model):
    ordering = ['due_back']

    def __str__(self):
        return '%s (%s)' % (self.id, self.book.title)
