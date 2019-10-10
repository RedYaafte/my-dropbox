from django.db import models


class Box(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    thing = models.FileField(upload_to='uploads/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
