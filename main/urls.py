from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index") ,
    path('teacher', views.teacher, name="teacher") ,
    path('eshghology', views.eshghology, name="eshghology"),
    path('your_talks', views.your_talks, name="your_talks"),
]
