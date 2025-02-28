from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.utils import timezone
from rest_framework import viewsets

from .models import Movie, Seat, Booking
from .forms import BookingForm
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

def index(request):
    print(request)
    template = loader.get_template("bookings/index.html")
    context = {}
    return render(request, "bookings/index.html", context)

def MovieViewSet(request):
    template = loader.get_template("bookings/movie_list.html")
    print(Movie.objects.all())
    context = {'movielist': Movie.objects.all()}
    return render(request, "bookings/movie_list.html", context)

def SeatViewSet(request, movie_id):
    seats = Seat.objects.all()
    movie = Movie.objects.get(pk=movie_id)
    booking = Booking.objects.all().filter(movie=movie)
    lst = []
    for book in booking:
        lst.append(book.seat.id)
    print(lst)
    context = {'Seats': seats, 'Movie': movie, 'Bookings': lst}
    return render(request, "bookings/seat_booking.html", context)


def BookingViewSet(request):
    template = loader.get_template("bookings/booking_history.html")
    test = Booking.objects.all()
    context = {'booking': test}
    return render(request, "bookings/booking_history.html", context)

def get_bookings(request, movie_id):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = BookingForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            Booking.objects.create(user=form.cleaned_data['your_name'], date=timezone.now(), movie=Movie.objects.get(pk=movie_id), seat=Seat.objects.get(pk=form.cleaned_data['your_seat']))
            # redirect to a new URL:
            return HttpResponseRedirect("/booking/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BookingForm()
    seats = Seat.objects.all()
    movie = Movie.objects.get(pk=movie_id)
    booking = Booking.objects.all().filter(movie=movie)
    lst = []
    for book in booking:
        lst.append(book.seat.id)
    context = {'Seats': seats, 'Movie': movie, 'Bookings': lst, "form": form}
    return render(request, "bookings/seat_booking.html", context)

class MovieAPIViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatAPIViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingAPIViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer