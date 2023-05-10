from rest_framework import serializers

from .models import Movie


class MovieSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name="movie-detail", lookup_field="slug")
    genre = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = "__all__"
        depth = 1

    def get_genre(self, obj):
        return [genre for genre in obj.genre.split()]


