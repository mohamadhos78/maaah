from django.db import models

# Create your models here.
class AnonymousTalk(models.Model):
    talk = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.talk[:40]