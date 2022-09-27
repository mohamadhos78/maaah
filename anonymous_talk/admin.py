from django.contrib import admin
from .models import AnonymousTalk, Reply
# Register your models here.



class AnonymousTalkAdmin(admin.ModelAdmin):
    list_display = ('id', 'talk', 'reply')

admin.site.register(AnonymousTalk, AnonymousTalkAdmin)
admin.site.register(Reply)