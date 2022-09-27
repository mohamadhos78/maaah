from django.contrib import admin
from .models import (
    GeneralInformation, Story, Report, Talk, Session, Teacher, Course, Video, Voice
)
admin.site.register(Story)

admin.site.register(Report)

class TalkAdmin(admin.ModelAdmin):  
    list_display = ('talk', 'name', 'is_published')
    list_editable = ('is_published', )
    list_filter = ('is_published',)
    list_per_page = 15
    

admin.site.register(Talk, TalkAdmin)


admin.site.register(Session)

admin.site.register(GeneralInformation)

admin.site.register(Teacher)

admin.site.register(Course)

admin.site.register(Video)

admin.site.register(Voice)
