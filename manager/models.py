from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    last_changed = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.name