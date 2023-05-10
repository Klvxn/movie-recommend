from django.urls import path

from .views import MoviesList, MovieDetail, APIRoot


urlpatterns = [
    path("", APIRoot.as_view()),
    path("movies/", MoviesList.as_view(), name="movie-list"),
    path("movies/<slug:slug>/", MovieDetail.as_view(), name="movie-detail")
]