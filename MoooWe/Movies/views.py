from django.shortcuts import render

# Create your views here.
def movies_home_page_view(request):
    return render(request , 'movies_home_page.html')