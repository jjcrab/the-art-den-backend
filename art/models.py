from django.db import models
from datetime import date


class Student(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='images/avatars', blank=True)
    school = models.CharField(max_length=150)
    graduation_year = models.PositiveSmallIntegerField()
    personal_story = models.TextField()

    def __str__(self):
        return self.name


class Artwork(models.Model):
    title = models.CharField(max_length=100)
    artwork_image = models.ImageField(upload_to='images/artworks', blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    pulication_date = models.DateField(default=date.today, blank=True)
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name='artworks')

    def __str__(self):
        return self.title
