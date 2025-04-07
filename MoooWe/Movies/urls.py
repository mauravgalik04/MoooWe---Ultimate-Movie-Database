from django.urls import path
from . import views

urlpatterns = [
    path('' , views.movies_home_page_view , name = 'movies_home_page')
]