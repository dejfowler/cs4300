from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from .models import Movie

def index(request):
    template = loader.get_template("bookings/index.html")
    context = {}
    return render(request, "bookings/index.html", context)

def MovieViewSet(request):
    template = loader.get_template("bookings/movie_list.html")
    print(Movie.objects.all())
    context = {}
    return render(request, "bookings/movie_list.html", context)

def MovieView(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, "polls/movies", {"movie": movie})

def SeatViewSet(request):
    template = loader.get_template("bookings/seat_booking.html")
    context = {}
    return render(request, "bookings/seat_booking.html", context)

def BookingViewSet(request):
    return HttpResponse("You're voting on question bookings")