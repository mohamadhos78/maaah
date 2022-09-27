from django.contrib import admin
from .models import AnonymousTalk, Reply
# Register your models here.



class AnonymousTalkAdmin(admin.ModelAdmin):
    list_display = ('id', 'talk', 'reply')
    list_display_links = ('id', 'talk')
    list_per_page = 15

admin.site.register(AnonymousTalk, AnonymousTalkAdmin)
admin.site.register(Reply)