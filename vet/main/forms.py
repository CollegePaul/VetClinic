from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["pet_name","animal","date","time"]
        widget = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "time": forms.TimeInput(attrs={"type" : "time"}),
        }
