from django.contrib import admin


from .models import Movie, Rating, DownloadLink, Actor, Director

# Register your models here.
admin.site.register(Movie)
admin.site.register(Rating)
admin.site.register(DownloadLink)
admin.site.register(Director)
admin.site.register(Actor)
