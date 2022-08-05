from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    description = models.CharField(max_length=512, null=True, blank=True)
    
    def __str__(self):
        return self.name


class Session(models.Model):
    title = models.CharField(max_length=64, null=False, blank=False)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    img = models.FileField(upload_to="sessions/img", null=True, blank=True)
    description = models.TextField()
    video = models.FileField(upload_to="sessions/video", null=True, blank=True)
    voice = models.FileField(upload_to="sessions/voice", null=True, blank=True)

    def __str__(self):
        return self.title
    

class Talk(models.Model):
    email = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=64, null=False, blank=False)
    talk = models.TextField(null=False, blank=False)
    date = models.DateField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    reply = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'دلنوشته'
        verbose_name_plural = 'دلنوشته ها'


class Teacher(models.Model):
    username = models.CharField(max_length=64, null=False, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=64, null=False, blank=False)


class Report(models.Model):
    title = models.CharField(max_length=64, null=False, blank=False, default="بدون توضیحات")
    description = models.TextField(null=False, blank=False)
    img = models.FileField(upload_to="reports/img", null=False, blank=False)
    video = models.FileField(upload_to="reports/video", null=True, blank=True)
    voice = models.FileField(upload_to="reports/voice", null=True, blank=True)

    def __str__(self):
        return self.title
    

class News(models.Model):
    img = models.FileField(upload_to="news/img", null=False, blank=False)
    text = models.CharField(max_length=128, null=False, blank=False, default="بدون توضیحات")

    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
