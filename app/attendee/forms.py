from django import forms
from .models import Attendee

SECTOR_CHOICES = (
        ('Privado', 'Privado' ),
        ('Publico', 'Publico'),
        )

class AttendeeForm(forms.ModelForm):
    sector = forms.CharField(
            max_length=30,
            widget=forms.Select(choices=SECTOR_CHOICES)
            )

    class Meta:
        model=Attendee
        fields = ['first_name', 'last_name','age', 'email', 'phone', 'sector']
