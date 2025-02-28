from django import forms


class BookingForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=20)
    your_seat = forms.IntegerField(label="Seat Number")