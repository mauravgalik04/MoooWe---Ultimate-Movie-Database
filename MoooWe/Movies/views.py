import os
from django.shortcuts import render , redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from Movies.models import Movie
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password


# Create your views here.

# Home Page view function : 
def movies_home_page_view(request):
    return render(request , 'movies_home_page.html')


# for displaying all the movies in a page : 
def movies_movies_view(request):
    query = request.GET.get('searchbar')
    if query:
        movies = Movie.objects.filter(name__icontains=query)
    else:
        movies = Movie.objects.all()
    data = {"movies": movies}
    return render(request, 'movies_movies.html', context=data)


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
@login_required 
def movies_feature_movie_view(request , id):
    movie = Movie.objects.get(id = id)
    data = {"movie" : movie}
    return render(request , 'movies_feature_movie.html' , context=data)

#for registering a user : 
def movies_register_view(request):
    User = get_user_model()
    if request.method == 'POST':
        name = request.POST.get('name').strip()
        email = request.POST.get('email').strip()
        phone = request.POST.get('phone').strip()
        address = request.POST.get('address').strip()
        gender = request.POST.get('gender').strip()
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        if password != cpassword:
            messages.error(request, 'Passwords do not match')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
        else:
            try:
                validate_password(password)
                User.objects.create_user(
                    email=email,
                    name=name,
                    phone=phone,
                    address=address,
                    gender=gender,
                    password=password
                )
                messages.success(request, 'Registration successful! You can now login.')
                print("Redirecting to login...")
                return redirect('movies_login')
            except ValidationError as e:
                for error in e:
                    messages.error(request, error)
            except Exception as e: # Catch any other error.
                messages.error(request, f"An unexpected error occurred: {e}") #provide the error to the user.
                print(f"An unexpected error occurred: {e}")
    return render(request, 'movies_register.html')

#for the user to log in:
def movies_login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email').strip()
        password = request.POST.get('password').strip()
        selected_role = request.POST.get('role')

        user = authenticate(request, email=email, password=password)

        if user:
            if (selected_role == 'admin' and user.is_superuser) or (selected_role == 'user' and not user.is_superuser):
                login(request, user)
                return redirect('movies_home_page')
            else:
                messages.error(request, "Role mismatch. Please select the correct role.")
        else:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'movies_login.html')
# for logging out :
@login_required 
def logout_view(request):
    logout(request)
    return redirect('movies_home_page') 

# for the profile page :
@login_required 
def movies_profile_view(request , id):
    return render(request , 'movies_profile.html')
@login_required 
def add_to_watchlist_view(request , id):
    movie = Movie.objects.get(id = id)
    movie.watchlist = 1
    movie.save()
    return redirect('movies_movies')
@login_required 
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