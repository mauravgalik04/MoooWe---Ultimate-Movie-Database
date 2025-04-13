import os
from django.shortcuts import render , redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from Movies.models import Movie
# Create your views here.

# Home Page view function : 
def movies_home_page_view(request):
    return render(request , 'movies_home_page.html')


# for displaying all the movies in a page : 
def movies_movies_view(request):
    movies = Movie.objects.all()
    data = {"movies":movies}
    return render(request , 'movies_movies.html' , context = data)


#for displaying movies in a genre wise manner : 
def movies_genre_view(request):
    genres = ['Action' , 'Adventure' , 'Biography' , 'Romance' , 'Comedy' , 'Drama' , 'Thriller' , 'Sci-Fi' , 'Crime' , 'Horror' , 'Other']
    movies = Movie.objects.all()
    data = {"genres":genres , "movies":movies}
    return render(request , 'movies_genre.html' , context=data)

def all_movie_in_genre_view(request , genre):
    movies = Movie.objects.filter(genre = genre)
    data = {"movies":movies , "genre" : genre}
    return render(request , "movie_all_movie_in_genre.html" , context = data)
#for displaying a single movies as featured movie :
def movies_feature_movie_view(request , id):
    movie = Movie.objects.get(id = id)
    data = {"movie" : movie}
    return render(request , 'movies_feature_movie.html' , context=data)

#for registering a user : 
def movies_register_view(request):
    return render(request , 'movies_register.html')

#for the user to log in:
def movies_login_view(request):
    return render(request , 'movies_login.html')

# for the profile page :
def movies_profile_view(request , id):
    return render(request , 'movies_profile.html')

def add_to_watchlist_view(request , id):
    movie = Movie.objects.get(id = id)
    movie.watchlist = 1
    movie.save()
    return redirect('movies_movies')
def remove_from_watchlist_view(request , id):
    movie = Movie.objects.get(id = id)
    movie.watchlist = 0
    movie.save()
    return redirect('movies_movies')
def movies_add_movie_view(request):
    if request.method == "POST":
        name = request.POST.get('movie-name')
        release_year = request.POST.get('release-year')
        genre = request.POST.get('genre')
        story = request.POST.get('movie-description')
        cast = request.POST.get('movie-cast')
        imdb_rating = request.POST.get('imdb-rating')
        poster = request.FILES.get('poster')
        landscape = request.FILES.get('landscape')

        upload_path = os.path.join(settings.BASE_DIR, 'Movies/static', 'uploads')
        os.makedirs(upload_path, exist_ok=True)

        fs = FileSystemStorage(location=upload_path)
        saved_poster = fs.save(poster.name, poster) if poster else None
        saved_landscape = fs.save(landscape.name, landscape) if landscape else None

        movie = Movie.objects.create(
            name=name,
            release_year=release_year,
            genre=genre,
            cast=cast,
            story=story,
            imdb_rating=imdb_rating,
            poster=saved_poster if saved_poster else None,
            landscape=saved_landscape if saved_landscape else None
        )

    return render(request , 'movies_add_movie.html')
def update_movie_view(request , id):
    movie = Movie.objects.get(id = id)
    if request.method == "POST":
        movie.name = request.POST.get('movie-name')
        movie.release_year = request.POST.get('release-year')
        movie.genre = request.POST.get('genre')
        movie.story = request.POST.get('movie-description')
        movie.cast = request.POST.get('movie-cast')
        movie.imdb_rating = request.POST.get('imdb-rating')
        movie.poster = request.FILES.get('poster') if request.FILES.get('poster') else movie.poster
        movie.landscape = request.FILES.get('landscape') if request.FILES.get('landscape') else movie.landscape
        movie.save()
        return redirect('movies_movies')
    data = {"movie" : movie}
    return render(request , 'movies_update_movie.html' , context = data)
def delete_movie_view(request , id):
    movie = Movie.objects.get(id = id)
    movie.delete()
    return redirect('movies_movies')