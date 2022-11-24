from rest_framework import serializers
from .models import Movie, MovieComment, Trend, Top, Genre
# from .models import Article, Comment
# 모델 데이터를 rest api에서 사용할 수 있게끔 json형식으로 바꿔준다.


class Genreserializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = ('name',)
        read_only_fields = ('movie',)


class MovieListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__' 

class MovieDetailSerializer(serializers.ModelSerializer):
    genres = Genreserializer(many=True, read_only=True)
    # genre_set = Genreserializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__' 

class TrendListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Trend
        fields = '__all__'

class TopListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Top
        fields = '__all__'

class MovieCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieComment
        fields = '__all__'
        read_only_fields = ('movie', )

