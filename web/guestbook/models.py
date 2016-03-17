from django.db import models


class Signature(models.Model):
    name = models.CharField(max_length=40)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
