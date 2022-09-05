from django.db import models
from random import randint


class AnonymousTalk(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    talk = models.TextField(null=False, blank=False)
    reply = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

    def save(self):
        if not self.id:
            is_unique = False
            while not is_unique:
                id = randint(10000, 1000000)
                is_unique = AnonymousTalk.objects.filter(id=id).exists()
            self.id = id
        super(AnonymousTalk, self).save()

    def __str__(self):
        return self.talk[:40]

    class Meta:
        verbose_name = 'پیام ناشناس'
        verbose_name_plural = 'پیام های ناشناس' 