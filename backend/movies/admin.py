from django.contrib import admin


from .models import Movie, Rating, Actor, Director

# Register your models here.
admin.site.register(Movie)
admin.site.register(Movie.DownloadQuality)
admin.site.register(Rating)
admin.site.register(Director)
admin.site.register(Actor)
