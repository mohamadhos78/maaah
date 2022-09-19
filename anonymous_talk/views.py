from django.shortcuts import render
from .forms import AnonymousTalkForm
from .models import AnonymousTalk
from django.contrib import messages

def send_message(request):
    if request.method == "POST":
        form = AnonymousTalkForm(request.POST)
        if form.is_valid():
            data = form.save()
        messages.success(request, 
            f"""پیام شما با موفقیت برای حاج اقا ارسال شد،
            شما می‌توانید از طریق {data.id} پاسخ حاج اقا را مشاهده کنید
            """
        )
    return render(request, "say-anonymous.html")

def see_answer(request):
    id = request.POST.get('message_id', None)
    if id:
        try:
            answer = AnonymousTalk.objects.get(id=id)
        except Exception as error:
            answer = None
            messages.error(
                request,
                "کد وارد شده صحیح نمی‌باشد"
                )
        else:
            if answer.reply:
                messages.success(
                    request, 
                    "نبریک میگم، حاج اقا به پیامت جواب داده"
                )
            else:
                messages.info(
                    request,
                    "متاسفانه هنوز به پیام شما پاسخی داده نشده است"
                    )
    else:
        answer = None
        
    context = {
        "id" : id,
        "answer" : answer
    }
    return render(request, "Haj_Agha's_answer.html", context)
