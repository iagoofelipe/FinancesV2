from django.db import models

class Auth(models.Model):
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)