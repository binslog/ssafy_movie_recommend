from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views



urlpatterns = [
    
    path('', views.movie_list),
    # path('<int:movie_pk>/', views.detail),
    path('trend/', views.trend_list),
    path('algo/', views.algo_list),
    path('top/', views.top_list),
    path('genre/', views.genre),
    
    path('<int:movie_id>/', views.movie_detail),
    path('<int:movie_id>/comments/', views.movie_comment_list),
    # path('movies/comments/', views.movie_comment_list),
    # path('<int:movie_id>/comments/<int:comment_pk>/', views.movie_comment_detail),
    path('<int:movie_id>/comments/create/', views.movie_comment_create),
]
