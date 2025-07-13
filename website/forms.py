from django import forms
from .models import Admission
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        exclude = ('selected_program',)
        fields = [
            'full_name', 'father_name', 'date_of_birth', 'gender', 'cnic_number', 
            'contact_number', 'email', 'address', 'highest_qualification', 
            'year_of_passing_matric', 'matric_institution',
            'scholarship', 'cnic_copy', 'passport_photo', 'matric_certificate',
            'payment_prof'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(AdmissionForm, self).__init__(*args, **kwargs)
        self.fields['address'].widget.attrs['row'] = '2' 

        self.fields['full_name'].widget.attrs['class'] = 'form-control'
        self.fields['full_name'].widget.attrs['placeholder'] = 'asad khan'
        self.fields['full_name'].widget.attrs['label'] = ''
        self.fields['full_name'].help_text = '<span class="form-text text-muted ">Write your good name here.</span>'

        self.fields['father_name'].widget.attrs['class'] = 'form-control'
        self.fields['father_name'].widget.attrs['placeholder'] = 'Sher Akbar'
        self.fields['father_name'].widget.attrs['label'] = ''
        self.fields['father_name'].help_text = '<span class="form-text text-muted ">Your fathers name here.</span>'

        self.fields['date_of_birth'].widget.attrs['class'] = 'form-control'
        self.fields['date_of_birth'].widget.attrs['placeholder'] = ''
        self.fields['date_of_birth'].widget.attrs['label'] = ''

        self.fields['gender'].widget.attrs['class'] = 'form-control'
        self.fields['gender'].widget.attrs['placeholder'] = ''
        self.fields['gender'].widget.attrs['label'] = ''
        

        self.fields['cnic_number'].widget.attrs['class'] = 'form-control'
        self.fields['cnic_number'].widget.attrs['placeholder'] = '11101-4567789-9'
        self.fields['cnic_number'].widget.attrs['label'] = ''
        self.fields['cnic_number'].help_text = '<span class="form-text text-muted ">Write your CNIC Number here</span>'
        
        self.fields['contact_number'].widget.attrs['class'] = 'form-control'
        self.fields['contact_number'].widget.attrs['placeholder'] = '0316-1210180'
        self.fields['contact_number'].widget.attrs['label'] = ''
        self.fields['contact_number'].help_text = '<span class="form-text text-muted ">Write your Phone Number here</span>'

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'example@gmail.com'
        self.fields['email'].widget.attrs['label'] = ''
        self.fields['email'].help_text = '<span class="form-text text-muted ">Write your email here</span>'

        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['placeholder'] = 'Bannu City'
        self.fields['address'].widget.attrs['label'] = ''
        self.fields['address'].help_text = '<span class="form-text text-muted ">Where are you from?</span>'

        self.fields['highest_qualification'].widget.attrs['class'] = 'form-control'
        self.fields['highest_qualification'].widget.attrs['placeholder'] = 'PHD'
        self.fields['highest_qualification'].widget.attrs['label'] = ''
        self.fields['highest_qualification'].help_text = '<span class="form-text text-muted ">Write your Highest digree/certificate here</span>'

        self.fields['year_of_passing_matric'].widget.attrs['class'] = 'form-control'
        self.fields['year_of_passing_matric'].widget.attrs['placeholder'] = '2019'
        self.fields['year_of_passing_matric'].widget.attrs['label'] = ''
        self.fields['year_of_passing_matric'].help_text = '<span class="form-text text-muted ">In which year do you pass your metric?</span>'

        self.fields['matric_institution'].widget.attrs['class'] = 'form-control'
        self.fields['matric_institution'].widget.attrs['placeholder'] = 'Bannu Board'
        self.fields['matric_institution'].widget.attrs['label'] = ''
        self.fields['matric_institution'].help_text = '<span class="form-text text-muted ">From which Board you passed your metric?</span>'

        self.fields['scholarship'].widget.attrs['class'] = 'form-control'
        self.fields['scholarship'].widget.attrs['placeholder'] = ''
        self.fields['scholarship'].widget.attrs['label'] = ''
        self.fields['scholarship'].help_text = '<span class="form-text text-muted ">Are you think that you are aligable to scholorship?</span>'

        self.fields['cnic_copy'].widget.attrs['class'] = 'form-control'
        self.fields['cnic_copy'].widget.attrs['placeholder'] = ''
        self.fields['cnic_copy'].widget.attrs['label'] = ''
        self.fields['cnic_copy'].help_text = '<span class="form-text text-muted ">upload your CNIC copy here.</span>'

        self.fields['passport_photo'].widget.attrs['class'] = 'form-control'
        self.fields['passport_photo'].widget.attrs['placeholder'] = ''
        self.fields['passport_photo'].widget.attrs['label'] = ''
        self.fields['passport_photo'].help_text = '<span class="form-text text-muted ">Upload your passport Size photo here.</span>'

        self.fields['matric_certificate'].widget.attrs['class'] = 'form-control'
        self.fields['matric_certificate'].widget.attrs['placeholder'] = ''
        self.fields['matric_certificate'].widget.attrs['label'] = ''
        self.fields['matric_certificate'].help_text = '<span class="form-text text-muted ">Upload your metric certificate here.</span>'

        self.fields['payment_prof'].widget.attrs['class'] = 'form-control'
        self.fields['payment_prof'].widget.attrs['placeholder'] = ''
        self.fields['payment_prof'].widget.attrs['label'] = ''
        self.fields['payment_prof'].help_text = '<span class="form-text text-muted ">Please pay us the amount of the program that you desire to enroll and upload the proof here.</span>'