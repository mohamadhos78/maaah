from django.urls import path
from . import views


urlpatterns = [
    path('', views.send_message, name="send-anonymous-message"), 
    path('answer/', views.see_answer, name="see-answer"),
    # path('answer/<str:id>/', views.see_answer, name="see-answer")
]