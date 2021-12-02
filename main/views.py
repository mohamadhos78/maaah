from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'landing.html', {})

def teacher(request):
    return render(request, 'teacher.html', {})
    
def eshghology(request):
    return render(request, 'eshghology.html', {})

def your_talks(request):
    return render(request, 'Your_talk.html', {})