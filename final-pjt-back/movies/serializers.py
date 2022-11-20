from rest_framework import serializers
from .models import Movie, Comment, Trend
# from .models import Article, Comment
# 모델 데이터를 rest api에서 사용할 수 있게끔 json형식으로 바꿔준다.
class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'vote_avg', 'poster_path')

class MovieDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__' 

class TrendListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Trend
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
