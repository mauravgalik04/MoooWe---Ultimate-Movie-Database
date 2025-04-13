from django.urls import path
from . import views

urlpatterns = [
    path('' , views.movies_home_page_view , name = 'movies_home_page'),
    path('movies/' , views.movies_movies_view , name = 'movies_movies'),
    path('genres/' , views.movies_genre_view , name = 'movies_genre'),
    path('genres/<str:genre>' , views.all_movie_in_genre_view , name = 'all_movies_in_genre'),
    path('feature_movie/<int:id>/' , views.movies_feature_movie_view , name = 'movies_feature_movie'),
    path('register/' , views.movies_register_view , name = 'movies_register'),
    path('login' , views.movies_login_view , name = 'movies_login'),
    path('profile/<int:id>' , views.movies_profile_view , name = 'movies_profile'),
    path('addmovie/' , views.movies_add_movie_view , name = 'movies_add_movie'),
    path('update_movie/<int:id>' , views.update_movie_view , name = 'update_movie'),
    path('delete_movie/<int:id>' , views.delete_movie_view , name = 'delete_movie'),
    path('add_to_watchlist/<int:id>' , views.add_to_watchlist_view , name = 'add_to_watchlist'),
    path('remove_from_watchlist/<int:id>' , views.remove_from_watchlist_view , name = 'remove_from_watchlist')
]