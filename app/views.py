from django.shortcuts import render
from app.forms import HeyForm

def root(request):
    return render(request, "root.html")

def hey(request):
    context = {}
    if request.method == "GET":
        form = HeyForm(request.GET)
        if form.is_valid():
            context['greating_success'] = True
    else:
        form = HeyForm()
    context['form'] = form
    return render(request, "hey.html", context)