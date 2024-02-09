from django import forms
from .models import Booking


class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForms(forms.ModelForm):
    class Meta:
        model =  Booking
        fields = '__all__'


        widgets = {
        'bookig_date':DateInput(),
    }

        labels = {
        'p_name':'Patient name',
        'p_phone':'Phone number',
        'p_email':'Email id',
        'doc_name':'Doctor name',
        'dep_name':'Department name',
        'booking_date':'Booking Date',
    }
