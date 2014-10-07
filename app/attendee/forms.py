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

    def __init__(self, *args, **kwargs):
        super(AttendeeForm, self).__init__(*args, **kwargs)
        #change the html class of all the elements of the form to get bootstrap 3 styling
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})
