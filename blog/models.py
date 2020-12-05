from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=120)
    time = models.DateTimeField(auto_now=True)
    blog = models.CharField(max_length=1024)


def __str__(self):
    return self.name
