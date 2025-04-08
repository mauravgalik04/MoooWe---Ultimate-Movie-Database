from django.shortcuts import render

# Create your views here.

# Home Page view function : 
def movies_home_page_view(request):
    return render(request , 'movies_home_page.html')


# for displaying all the movies in a page : 
def movies_movies_view(request):
    return render(request , 'movies_movies.html')


#for displaying movies in a genre wise manner : 
def movies_genre_view(request):
    return render(request , 'movies_genre.html')

#for displaying a single movies as featured movie :
def movies_feature_movie_view(request , sno):
    return render(request , 'movies_feature_movie.html')

#for registering a user : 
def movies_register_view(request):
    return render(request , 'movies_register.html')

#for the user to log in:
def movies_login_view(request):
    return render(request , 'movies_login.html')

# for the profile page :
def movies_profile_view(request , id):
    return render(request , 'movies_profile.html')