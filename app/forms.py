from django import forms

class HeyForm(forms.Form):
    name = forms.CharField(max_length=80)
