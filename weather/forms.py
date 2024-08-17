from django import forms

class LocationForm(forms.Form):
    location = forms.CharField(max_length=50, label="",widget=forms.TextInput(attrs={'placeholder':'Enter City'}))
