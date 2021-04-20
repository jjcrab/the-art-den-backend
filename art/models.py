from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date
from student_users.models import Studentuser


def current_year():
    return date.today().year


class Student(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.ImageField(
        upload_to='images/avatars', blank=True, default='images/avatars/noavatardefault.jpeg')
    school = models.CharField(max_length=150)
    graduation_year = models.PositiveSmallIntegerField(
        default=current_year, validators=[MinValueValidator(2019), MaxValueValidator(2030)])
    personal_story = models.TextField()

    def __str__(self):
        return self.name


class Artwork(models.Model):
    title = models.CharField(max_length=100)
    artwork_image = models.ImageField(
        upload_to='images/artworks', blank=True, default='images/artworks/noImageAvailable.jpeg')
    price = models.DecimalField(max_digits=12, decimal_places=2)
    pulication_date = models.DateField(default=date.today, blank=True)
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name='artworks')
    owner = models.ForeignKey(
        Studentuser, related_name='owned_artworks', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
