from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    description = models.CharField(max_length=512, null=True, blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'دوره'
        verbose_name_plural = 'دوره ها'


class Session(models.Model):
    title = models.CharField(max_length=64, null=False, blank=False)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    img = models.FileField(upload_to="sessions/img", null=True, blank=True)
    description = models.TextField()
    video = models.FileField(upload_to="sessions/video", null=True, blank=True)
    voice = models.FileField(upload_to="sessions/voice", null=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'جلسه'
        verbose_name_plural = 'جلسات'

class Talk(models.Model):
    email = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=64, null=False, blank=False)
    talk = models.TextField(null=False, blank=False)
    date = models.DateField(auto_now_add=True, )
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

    class Meta:
        verbose_name = 'گزارش'
        verbose_name_plural = 'گزارش ها'
    

class Story(models.Model):
    img = models.FileField(upload_to="news/img", null=False, blank=False)
    text = models.CharField(max_length=128, null=False, blank=False, default="بدون توضیحات")

    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name = 'خبر'
        verbose_name_plural = 'اخبار'

class GeneralInformation(models.Model):
    title = models.CharField(max_length=25, null=False, blank=False)
    description = models.TextField()
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    instagram = models.URLField(max_length=250, null=True, blank=True)
    telegram = models.URLField(max_length=250, null=True, blank=True)
    eitaa = models.URLField(max_length=250, null=True, blank=True)

    def __str__(self):
        return "اطلاعات کلی سایت"

class Video(models.Model):
    title = models.CharField(max_length=70, null=False, blank=False)
    description = models.TextField()
    file = models.FileField(upload_to="videos", null=False, blank=False)

    def __str__(self):
        return self.title


class Voice(models.Model):
    title = models.CharField(max_length=70, null=False, blank=False)
    description = models.TextField()
    file = models.FileField(upload_to="voices", null=False, blank=False)

    def __str__(self):
        return self.title