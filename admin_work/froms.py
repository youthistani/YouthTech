from django import forms
from website.models import ResultDocument


class ResultUploadForm(forms.Form):
     class Meta:
        model = ResultDocument
        fields = ['pdf_file']
        widgets = {
            'pdf_file': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }