from django import forms
from .models import Ord


class OrderForm(forms.ModelForm):
    class Meta:
        model = Ord
        fields = [
            'first_name',
            'last_name',
            'phone', 
            'email', 
            'address_line_1', 
            'address_line_2', 
            'country', 
            'city', 
            'order_note',
            ]