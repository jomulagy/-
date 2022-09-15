from django.db import models
from datetime import datetime, timedelta

class Post(models.Model):
    board = models.CharField(max_length=100,default='')
    likes = models.IntegerField(default = 0)
    annonymous = models.BooleanField(default = False)
    user = models.ForeignKey('account.myUser',null=True,on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField()
    title = models.TextField(default = '')
    content = models.TextField(null=True)
    image = models.ImageField(upload_to='images/',blank=True)

    @property
    def created_string(self):

        time = datetime.now() - self.time

        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = datetime.now().date() - self.time.date()
            return str(time.days) + '일 전'
        else:
            return False
    @property
    def writer(self):
        if self.annonymous:
            return '익명'
        else:
            return self.user.first_name+self.user.last_name
            
    
    @property
    def get_time(self):
        time = ''
        month = str(self.time.month)
        if len(month)==1:
            month = '0'+month
        day = str(self.time.day)
        if len(day)==1:
            day = '0'+day
        hour = str(self.time.hour)
        if len(hour)==1:
            hour = '0'+hour
        minute = str(self.time.minute)
        if len(minute)==1:
            minute = '0'+minute
        
        time = month + '/' + day + ' ' + hour + ":" + minute
        return time;
    
