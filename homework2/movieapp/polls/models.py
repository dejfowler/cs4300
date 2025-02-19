from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    Description = models.CharField(max_length=200)
    date = models.DateTimeField("date released")
    duration = models.IntegerField(default=0)

class Seat(models.Model):
    seat_number = models.IntegerField(default=0)
    status = models.BooleanField(default=False)

class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.CharField(max_length=20)
    date = models.DateTimeField("date booked")