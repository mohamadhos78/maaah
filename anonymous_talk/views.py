from django.shortcuts import render
from .forms import AnonymousTalkForm
# Create your views here.

def send_message(request):
    if request.method == "POST":
        form = AnonymousTalkForm(request.POST)
        if form.is_valid():
            data = form.save()
    return render(request, "say-anonymous.html")
