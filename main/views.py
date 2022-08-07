from django.shortcuts import render
from .models import Story, Report, Talk, Session
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q

def index(request):
    stories = Story.objects.all()
    reports = Report.objects.all()
    context ={
        "stories" : stories,
        "reports" : reports,
    }
    return render(request, 'landing.html', context)

@login_required
def teacher(request):
    sessions = Session.objects.all()
    context ={
        "sessions" : sessions ,
    }
    return render(request, 'teacher.html', context)
    
def courses(request):
    q = request.GET.get('q')
    name = request.GET.get('name')
    if q:
        sessions = Session.objects.filter(Q(description__icontains=q) | Q(description__icontains=q))
    elif name:
        sessions = Session.objects.filter(Q(description__contains=name))
    else:
        sessions = Session.objects.all()

    context ={
        "sessions" : sessions ,
    }
    return render(request, 'eshghology.html', context)

def your_talks(request):

    if request.method == "POST":
        from .forms import TalkForm
        talk_form = TalkForm(request.POST)
        if talk_form.is_valid():
            talk_form.save()

    talks = reversed(Talk.objects.filter(is_published=True))

    context = {
        "talks" : talks,
    }
    return render(request, 'Your_talk.html', context)