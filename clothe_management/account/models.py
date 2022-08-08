from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

# Create your models here.
class myUser(AbstractUser):
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    image = models.ImageField(upload_to = 'images/',default = "/static/img/account.png")

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password

    @property
    def get_date_joined(self):
        time = ''
        year = str(self.date_joined.year)
        month = str(self.date_joined.month)
        if len(month)==1:
            month = '0'+month
        day = str(self.date_joined.day)
        if len(day)==1:
            day = '0'+day
        
        time = year + '.' + month + '.' + day
        return time;      