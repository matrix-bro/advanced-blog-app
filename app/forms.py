from django import forms

class PostShareForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)   # Recommended by this person
    to = forms.EmailField(max_length=100)       # Recommended to this person
    comments = forms.CharField(required=False, widget=forms.Textarea)