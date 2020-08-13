from django.contrib.auth.models import User
from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Register(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='user')
    phone=models.IntegerField()


