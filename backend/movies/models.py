import autoslug
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.shortcuts import reverse


# Create your models here.
class Movie(models.Model):

    class MovieType(models.TextChoices):
        SERIES = "Series"
        SINGLE = "Single"

    class DownloadQuality(models.Model):
        standard = models.URLField()
        high = models.URLField()

    type = models.CharField(max_length=30, choices=MovieType.choices, null=True)
    slug = autoslug.AutoSlugField(
        populate_from="title", always_update=True, unique=True, primary_key=True
    )
    title = models.CharField(max_length=100)
    desc = models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length=200)
    pahe = models.ForeignKey(
        DownloadQuality,
        related_name="pahe_link",
        on_delete=models.SET_NULL,
        null=True
    )
    torrent = models.ForeignKey(
        DownloadQuality,
        related_name="torrent_quality",
        on_delete=models.SET_NULL,
        null=True
    )
    duration = models.DurationField()
    cover_photo = models.ImageField(upload_to="cover")
    ratings = models.ForeignKey("Rating", on_delete=models.SET(None))
    directors = models.ManyToManyField("Director", related_name="movie_directors")
    actors = models.ManyToManyField("Actor", related_name="movie_actors")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie-detail", args=[self.slug])


class Rating(models.Model):

    rotten_tomatoes = models.CharField(max_length=10)
    ours = models.CharField(max_length=10)
    imdb = models.CharField(max_length=10)


class Person(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    class Meta:
        abstract = True

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.get_full_name()


class Director(Person):
    pass


class Actor(Person):
    pass


class CustomUser(AbstractUser):
    pass
