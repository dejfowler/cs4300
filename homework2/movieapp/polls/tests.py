from django.test import TestCase
from django.utils import timezone

from .models import Movie, Seat, Booking


class MovieModelTests(TestCase):
    def test_movie_model(self):
            test = Movie(title="Forrest Gump", Description="Hello", id=1, date=1995, duration=95)
            self.assertIs(type(test.title), str)
            self.assertIs(type(test.date), int)
            self.assertIs(type(test.duration), int)

class SeatModelTests(TestCase):
    def test_seat_model(self):
            test = Seat(seat_number=1, status=True)
            self.assertIs(type(test.seat_number), int)
            self.assertIs(type(test.status), bool)

class BookingModelTests(TestCase):
    def test_booking_model(self):
            testone = Movie(title="Forrest Gump", Description="Hello", id=1, date=1995, duration=95)
            testtwo = Seat(seat_number=1, status=True)
            testthree = Booking(user="Me", date=timezone.now(), id=1, movie=testone, seat=testtwo)
            self.assertIs(type(testthree.movie), type(Movie()))
            self.assertIs(type(testthree.seat), type(Seat()))
            self.assertIs(type(testthree.user), str)