from django import forms
from app.models.blog import Comment

INPUT_CLASSES = 'w-full py-2 px-3 rounded-md border'

class PostShareForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'John Doe',
        'class': INPUT_CLASSES
    }))

    # Recommended by this person
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={
        'placeholder': 'youremail@gmail.com',
        'class': INPUT_CLASSES
    }))   

    # Recommended to this person
    to = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={
        'placeholder': 'yourfriendemail@gmail.com',
        'class': INPUT_CLASSES
    }))   

    comments = forms.CharField(required=False, widget=forms.Textarea(attrs={
        'placeholder': 'Any comments...',
        'class': INPUT_CLASSES
    }))

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']

    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'John Doe',
        'class': INPUT_CLASSES
    }))

    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={
        'placeholder': 'john@gmail.com',
        'class': INPUT_CLASSES
    }))

    body = forms.CharField(required=False, widget=forms.Textarea(attrs={
        'placeholder': 'Join the discussion...',
        'class': INPUT_CLASSES
    }))

class SearchForm(forms.Form):
    query = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Search here',
        'class': 'w-full'
    }))    