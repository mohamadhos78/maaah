from django.shortcuts import render
from .forms import AnonymousTalkForm
from .models import AnonymousTalk

def send_message(request):
    if request.method == "POST":
        form = AnonymousTalkForm(request.POST)
        if form.is_valid():
            data = form.save()
            print(data.id)
    return render(request, "say-anonymous.html")

def see_answer(request):
    id = request.POST.get('message_id', None)
    if id:
        answer = AnonymousTalk.objects.get(id=id)
    else:
        answer = None
        
    context = {
        "id" : id,
        "answer" : answer
    }
    return render(request, "Haj_Agha's_answer.html", context)
