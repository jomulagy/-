from distutils.command.upload import upload
from turtle import color
from django.db import models

class clothe(models.Model):
    user = models.ForeignKey('account.myUser',on_delete=models.CASCADE)
    name = models.TextField(null=False, default = '')
    image = models.ImageField(upload_to='images/')
    season = models.TextField()
    parent_category = models.TextField(default='')
    child_category = models.TextField(default='')
    favorite = models.BooleanField(default=False)
    color = models.TextField()
    style = models.TextField()
    memo = models.TextField()