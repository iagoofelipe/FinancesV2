from django.db import models
from ..login.models import Auth

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    auth = models.ForeignKey(Auth, models.CASCADE)