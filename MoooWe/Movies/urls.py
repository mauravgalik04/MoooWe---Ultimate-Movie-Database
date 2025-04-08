from django.urls import path
from . import views

urlpatterns = [
    path('' , views.movies_home_page_view , name = 'movies_home_page'),
    path('/movies/' , views.movies_movies_view , name = 'movies_movies'),
    path('/genres/' , views.movies_genre_view , name = 'movies_genre'),
    path('/feature_movie/<int:sno>/' , views.movies_feature_movie_view , name = 'movies_feature_movie'),
    path('/register/' , views.movies_register_view , name = 'movies_register'),
    path('/login' , views.movies_login_view , name = 'movies_login'),
    path('/profile/<int:id>' , views.movies_profile_view , name = 'movies_profile'),
]