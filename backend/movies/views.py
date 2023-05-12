from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Movie
from .serializers import MovieSerializer


# Create your views here.
class APIRoot(APIView):

    def get(self, request, format=None):
        return Response({
            "Movies": reverse("movie-list", request=request, format=format),
        })


class MoviesList(ListAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filterset_fields = ["genre", "directors"]
    search_fields = [
        "directors__first_name",
        "directors__last_name",
        "actors__last_name",
        "actors__first_name",
        "title"
    ]


class MovieDetail(RetrieveAPIView):

    lookup_field = "slug"
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
