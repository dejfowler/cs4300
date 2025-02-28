from .models import Movie, Booking, Seat
from rest_framework import serializers


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ['url', 'title', 'Description', 'date', 'duration']


class SeatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seat
        fields = ['url', 'seat_number', 'status']

class BookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booking
        fields = ['url', 'user', 'movie', 'seat', 'date']