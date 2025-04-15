from django.urls import path
from . import views
urlpatterns = [
    path('' , views.booking_home_view , name = "booking_home"),
    path('theatre_dashboard/' , views.theater_dashboard_view , name = "theatre_dashboard"),
    path('theatre_register/' , views.register_theatre_view , name = 'theatre_registration')
]