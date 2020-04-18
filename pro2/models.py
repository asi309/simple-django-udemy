from django.db import models

# Create your models here.
class User(models.Model):
    fname = models.CharField(max_length=15)
    lname = models.CharField(max_length=20)
    email = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return str(self.email)