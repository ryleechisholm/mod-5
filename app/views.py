from django.shortcuts import render
from app.forms import HeyForm, HowOld, OrderForm

def root(request):
    return render(request, "root.html")

def hey(request):
    form = HeyForm(request.GET)
    if form.is_valid():
        name = form.cleaned_data['name']
        return render(request, 'hey.html', {"form": form, "name": name})
    form = HeyForm()
    return render(request, "hey.html", {"form": form})

def age_in(request):
    form = HowOld(request.GET)
    if form.is_valid():
        year = form.cleaned_data['year']
        birthyear = form.cleaned_data['birthyear']
        age = year - birthyear
        return render(request, "age-in.html", {"form": form, "age": age, "year": year})
    form = HowOld()
    return render(request, "age-in.html", {"form": form})

def order(request):
    form = OrderForm(request.GET)
    if form.is_valid():
        burgers = form.cleaned_data['burgers']
        drinks = form.cleaned_data['drinks']
        fries = form.cleaned_data['fries']
        total = (burgers * 4.5) + (fries * 1.5) + drinks
        return render(request, "order.html", {"form": form, "total": total})
    form = OrderForm()
    return render(request, "order.html", {"form": form})
