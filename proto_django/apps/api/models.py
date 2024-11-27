from django.db import models
from django.contrib.auth.models import User

from src import consts

class Category(models.Model):
    inout = models.IntegerField(choices=consts.TYPES_INOUT, default=0, null=False)
    name = models.TextField(max_length=45)

class Registry(models.Model):
    inout = models.IntegerField(choices=consts.TYPES_INOUT, default=0, null=False)
    title = models.TextField(max_length=45, null=True)
    datetime = models.DateTimeField()
    value = models.DecimalField(decimal_places=2, max_digits=11, default=0.0)
    description = models.TextField(max_length=255, null=True)
    categories = models.ManyToManyField(Category)

class Profile(models.Model):
    name = models.TextField(max_length=45, default='perfil principal')
    users = models.ManyToManyField(User, through='UserProfileRules')
    registries = models.ManyToManyField(Registry)

class UserProfileRules(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    owner = models.BooleanField(default=True)
    edit = models.BooleanField(default=True)
    read = models.BooleanField(default=True)