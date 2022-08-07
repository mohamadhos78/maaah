from django.contrib import admin
from django.utils.html import format_html
from .models import GeneralInformation, News, Report, Talk, Session, Teacher, Course

admin.site.register(News)

admin.site.register(Report)

class TalkAdmin(admin.ModelAdmin):
    list_display = ('talk', 'name', 'is_published')
    list_filter = ('is_published',)
    

admin.site.register(Talk, TalkAdmin)


admin.site.register(Session)

admin.site.register(GeneralInformation)

admin.site.register(Teacher)

admin.site.register(Course)
