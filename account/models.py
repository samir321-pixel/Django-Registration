from django.db import models
from django.db.models import ForeignKey
from django.contrib.auth.models import User


# Create your models here.
class Account(models.Model):
    user = ForeignKey(User, on_delete=models.DO_NOTHING)
