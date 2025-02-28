from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from .models import Movie, Seat

def index(request):
    template = loader.get_template("bookings/index.html")
    context = {}
    return render(request, "bookings/index.html", context)

def MovieViewSet(request):
    template = loader.get_template("bookings/movie_list.html")
    print(Movie.objects.all())
    context = {'movielist': Movie.objects.all()}
    return render(request, "bookings/movie_list.html", context)

def SeatViewSet(request):
    template = loader.get_template("bookings/seat_booking.html")
    seats = Seat.objects.all()
    movie = Movie.objects.get(pk=1)
    context = {'Seats': seats, 'Movie': movie}
    return render(request, "bookings/seat_booking.html", context)

def BookingViewSet(request):
    template = loader.get_template("bookings/booking_history.html")
    context = {}
    return render(request, "bookings/booking_history.html", context)