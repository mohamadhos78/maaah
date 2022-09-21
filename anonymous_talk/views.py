from django.shortcuts import render, get_object_or_404
from .forms import AnonymousTalkForm
from .models import AnonymousTalk
from main.models import GeneralInformation
from django.contrib import messages

def send_message(request):
    if request.method == "POST":
        form = AnonymousTalkForm(request.POST)
        if form.is_valid():
            data = form.save()
        messages.success(request, 
            f"""پیام شما با موفقیت برای حاج آقا ارسال شد،
            شما می‌توانید از طریق {data.id} 
            پاسخ حاج آقا را مشاهده کنید.
            
            توجه داشته باشید کد مشاهده پاسخ قابل بازیابی نمی باشد در حفظ آن کوشا باشید.
            """
        )
    
    home_page_information = get_object_or_404(GeneralInformation, id=1)
    context = {
        "home_page_information" : home_page_information
    }
    return render(request, "say-anonymous.html", context)

def see_answer(request):
    id = request.POST.get('message_id', None)
    if id:
        try:
            answer = AnonymousTalk.objects.get(id=id)
        except Exception as error:
            answer = None
            messages.error(
                request,
                "کد وارد شده صحیح نمی باشد."
                )
        else:
            if answer.reply:
                messages.success(
                    request, 
                    "تبریک میگم ، حاج آقا به پیامت جواب داده"
                )
            else:
                messages.info(
                    request,
                   " متاسفانه هنوز به پیام شما پاسخی داده نشده است."
                    )
    else:
        answer = None
    home_page_information = get_object_or_404(GeneralInformation, id=1)
        
    context = {
        "id" : id,
        "answer" : answer,
        "home_page_information" : home_page_information
    }
    return render(request, "Haj_Agha's_answer.html", context)
