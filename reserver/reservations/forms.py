from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model= Reservation
        fields =['name', 'date', 'time', 'table_size']
        widgets= {'date': forms.DateInput(attrs={'type': 'date'}),
                  'time': forms.TimeInput(attrs={'type': 'time'}),}