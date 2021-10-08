from django import forms

class HeyForm(forms.Form):
    name = forms.CharField(max_length=80)

class HowOld(forms.Form):
    year = forms.IntegerField()
    birthyear = forms.IntegerField()

class OrderForm(forms.Form):
    burgers = forms.IntegerField()
    drinks = forms.IntegerField()
    fries = forms.IntegerField()
