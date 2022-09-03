from django.db import models
import uuid


class AnonymousTalk(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    talk = models.TextField(null=False, blank=False)
    reply = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

    def __str__(self):
        return self.talk[:40]

    class Meta:
        verbose_name = 'پیام ناشناس'
        verbose_name_plural = 'پیام های ناشناس' 