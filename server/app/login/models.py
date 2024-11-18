from django.db import models

class Auth(models.Model):
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)