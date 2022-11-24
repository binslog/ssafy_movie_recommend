
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from movies.serializers import MovieListSerializer , MovieDetailSerializer,  TrendListSerializer, MovieCommentSerializer, TopListSerializer, Genreserializer

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Movie, MovieComment, Trend, Top, Genre
 

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
def algo_list(request):
    movies = Movie.objects.order_by('-vote_avg').prefetch_related('genres')[:20]
    serializer = TrendListSerializer(movies, many=True)   
    return Response(serializer.data)

@api_view(['GET'])
def top_list(request):
    movies = Top.objects.all()
    serializer = TopListSerializer(movies, many=True)   
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    # comments = movie.comment_set.all()
    # 역참조한 comments정보를 어떻게 serializer로 같이 보내줄까?
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def movie_comment_list(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    comments = MovieComment.objects.all()
    serializer = MovieCommentSerializer(comments, many=True)   
    return Response(serializer.data)

@api_view(['GET'])
def genre(request):
    genre = Genre.objects.all()
    
    serializer = Genreserializer(genre, many=True)   
    return Response(serializer.data)


# @api_view(['GET'])
# def argomovie_list(request):
#     movies = Movie.objects.all()
    
#     serializer = MovieListSerializer(movies, many=True)   
#     return Response(serializer.data)


# 이 두 개가 필요한가?
# 위는 모든 movie의 덧글을 출력해주는 코드
# 아래는 개개의 무비덧글을 출력해주는 코드

# @api_view(['GET', 'DELETE', 'PUT'])
# movie_id 인지 movie_pk인지 확인해보기
# def movie_comment_detail(request, movie_id):
#     # comment = Comment.objects.get(pk=comment_pk)
#     comment = get_object_or_404(MovieComment, pk=comment_pk)

#     if request.method == 'GET':
#         serializer = MovieCommentSerializer(comment)
#         return Response(serializer.data)
# ## 아래코드를 프로젝트 특성에 맞도록 사용하지 않습니다.
#     elif request.method == 'DELETE':
#         comment.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     elif request.method == 'PUT':
#         serializer = MovieCommentSerializer(comment, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)

@api_view(['POST','GET'])
#  movie_id 인지 movie_pk인지 확인해보기
def movie_comment_create(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    serializer = MovieCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return  Response(serializer.data, status=status.HTTP_201_CREATED)