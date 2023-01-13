from django.db import models

# Create your models here.

class Contact(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=34)
    password = models.TextField()
    phone = models.CharField(max_length=30)

    def __str__(self):
        return self.username