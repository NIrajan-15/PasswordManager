from django.utils import timezone
from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    

    last_changed = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class UpdateHistory(models.Model):
    name = models.EmailField(blank=True,null=True)
    updated_column = models.CharField(max_length=200,blank=True,null=True)
    updated_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name