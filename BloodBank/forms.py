from django import forms
from .models import Donor

class DonorRegistrationForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['name', 'phone', 'age', 'blood_group','address']
    def __init__(self, *args, **kwargs):
        super(DonorRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['address'].widget.attrs['row'] = '2'
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})