from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=50, verbose_name="제목")
    release = models.IntegerField(verbose_name="개봉년도")
    GENRE_CHOICES = [
        ('AC', 'Action'),
        ('DR', 'Drama'),
        ('CM', 'Comedy'),
        ('RM', 'Romance'),
        ('TH','Thriller'),
        ('HR','Horror'),
        ('SF','SF'),
        ('FT','Fantasy'),
    ]
    genre = models.CharField(max_length=50, verbose_name="장르", choices=GENRE_CHOICES)
    rating = models.FloatField(verbose_name="별점")
    time = models.IntegerField(verbose_name="러닝타임")
    review = models.TextField(verbose_name="리뷰")
    director = models.CharField(max_length=50, verbose_name="감독")
    actor = models.CharField(max_length=50, verbose_name="배우")