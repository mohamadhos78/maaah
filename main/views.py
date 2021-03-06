from django.shortcuts import render
from .models import News, Report, Talk, Session
from django.contrib.auth.decorators import login_required

def index(request):
    news = News.objects.all()
    reports = Report.objects.all()
    context ={
        "news" : news,
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
    
def eshghology(request):
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

    talks = reversed(Talk.objects.all())

    context = {
        "talks" : talks,
    }
    return render(request, 'Your_talk.html', context)