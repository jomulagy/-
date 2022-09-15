from django.db import models
from datetime import datetime,timedelta

class ChatRoom(models.Model):
    users = models.ManyToManyField('account.myUser')
    annonymous = models.BooleanField(default = False)

class Message(models.Model):
    user = models.ForeignKey('account.myUser',on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    chatroom = models.ForeignKey(ChatRoom,on_delete=models.CASCADE)
    read = models.BooleanField(null=False,default = False)

    @property
    def get_time(self):
        time = datetime.now() - self.time
        result = ''
        if len(str(self.time.month))==1:
            result+='0'
        result+=str(self.time.month)+'/'
        if len(str(self.time.day))==1:
            result+='0'
        result+=str(self.time.day)+' '
        if len(str(self.time.hour))==1:
            result+='0'
        result+=str(self.time.hour)+":"
        if len(str(self.time.minute))==1:
            result+='0'
        result+=str(self.time.minute)

        if time < timedelta(days=365):
            return result
        else:
            return str(self.time.year)+result
