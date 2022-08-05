from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name="index") ,
    path('teacher', views.teacher, name="teacher") ,
    path('courses', views.courses, name="courses"),
    path('your_talks', views.your_talks, name="your_talks"),
]

