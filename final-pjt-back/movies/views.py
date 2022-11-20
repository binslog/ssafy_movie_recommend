
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from movies.serializers import MovieListSerializer , MovieDetailSerializer, CommentSerializer, TrendListSerializer

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Movie, Comment, Trend
 

# 영화 리스트
# 221017(월)_코딩 Live 강의 Python 트랙_오후_5_Build RESTful API - Article 20분까지 체크함!
@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)   
    return Response(serializer.data)
    
@api_view(['GET'])
def trend_list(request):
    movies = Trend.objects.all()
    serializer = TrendListSerializer(movies, many=True)   
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    # comments = movie.comment_set.all()
    # 역참조한 comments정보를 어떻게 serializer로 같이 보내줄까?
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def comment_list(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)   
    return Response(serializer.data)