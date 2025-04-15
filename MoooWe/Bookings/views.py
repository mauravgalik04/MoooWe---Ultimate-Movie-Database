import os
from django.shortcuts import render
from Movies.models import Movie
from django.conf import settings
from Bookings.models import Theatre
import random
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
# Create your views here.
@login_required 
def booking_home_view(request):
    query = request.GET.get('searchbar')
    if query:
        movies = Movie.objects.filter(name__icontains=query)
    else:
        movies = Movie.objects.all()
    data = {"movies": movies}
    return render(request, 'booking_home_page.html', context=data)

def theater_dashboard_view(request):
    theatres = Theatre.objects.all()
    data = {"theatres" : theatres}
    return render(request , 'theatre_dashboard.html' , context=data)
def register_theatre_view(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        theatre = Theatre.objects.create(
            image=image,
            name=request.POST.get('theatre-name'),
            location=request.POST.get('location'),
            capacity=request.POST.get('capacity'),
            gold_seats=request.POST.get('gold-seats'),
            gold_price=request.POST.get('gold-price'),
            silver_seats=request.POST.get('silver-seats'),
            silver_price=request.POST.get('silver-price'),
            bronze_seats=request.POST.get('bronze-seats'),
            bronze_price=request.POST.get('bronze-price'),
            owner_id=request.user.id
        )
    return render(request, 'theatre_registration.html')