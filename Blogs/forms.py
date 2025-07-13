from .models import BlogPost, Comments
from django import forms


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'category']
    
    def __init__(self, *args, **kwargs):
        super(BlogPostForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder'] = 'Data Science'
        self.fields['title'].widget.attrs['label'] = ''

        self.fields['content'].widget.attrs['class'] = 'form-control'
        self.fields['content'].widget.attrs['placeholder'] = 'Your thoughts'
        self.fields['content'].widget.attrs['label'] = ''

        self.fields['category'].widget.attrs['class'] = 'form-control'
        self.fields['category'].widget.attrs['placeholder'] = ''
        self.fields['category'].widget.attrs['label'] = ''

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super(CommentsForm, self).__init__(*args, **kwargs)

        self.fields['content'].widget.attrs['class'] = 'form-control'
        self.fields['content'].widget.attrs['placeholder'] = 'Your thoughts'
        self.fields['content'].widget.attrs['label'] = ''