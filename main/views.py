from django.shortcuts import render
from .models import (
    Story, Report, Talk, Session, GeneralInformation, Video, Voice
    )
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q


@login_required(login_url="/admin/")
def index(request):
    home_page_information = get_object_or_404(GeneralInformation, id=1)
    stories = Story.objects.all()
    reports = Report.objects.all()
    videos = Video.objects.all()
    voices = Voice.objects.all()
    context ={
        "stories" : stories,
        "reports" : reports,
        "home_page_information" : home_page_information,
        "videos" : videos ,
        "voices" : voices 
    }
    return render(request, 'landing.html', context)

@login_required(login_url="/admin/")
def teacher(request):
    sessions = Session.objects.all()
    context ={
        "sessions" : sessions ,
    }
    return render(request, 'teacher.html', context)

@login_required(login_url="/admin/")    
def courses(request):
    q = request.GET.get('q')
    name = request.GET.get('name')
    home_page_information = get_object_or_404(GeneralInformation, id=1)
    if q:
        sessions = Session.objects.filter(Q(description__icontains=q) | Q(description__icontains=q))
    elif name:
        sessions = Session.objects.filter(Q(description__contains=name))
    else:
        sessions = Session.objects.all()

    context ={
        "sessions" : sessions ,
        "home_page_information" : home_page_information
    }
    return render(request, 'eshghology.html', context)

@login_required(login_url="/admin/")
def your_talks(request):

    if request.method == "POST":
        from .forms import TalkForm
        talk_form = TalkForm(request.POST)
        if talk_form.is_valid():
            talk_form.save()

    talks = reversed(Talk.objects.filter(is_published=True))
    home_page_information = get_object_or_404(GeneralInformation, id=1)

    context = {
        "talks" : talks,
        "home_page_information" : home_page_information,
    }
    return render(request, 'Your_talk.html', context)