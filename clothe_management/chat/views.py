from django.shortcuts import redirect, render
from .forms import MessageForm
from account.models import myUser
from .models import ChatRoom, Message
# Create your views here.
def chatting(request,chatroom_id):
    chatrooms = [chatroom for chatroom in ChatRoom.objects.filter(users__id = request.user.id).all()]
    context = {
        'chatrooms' : chatrooms,
        }
    if chatroom_id != '0':
        chats = Message.objects.filter(chatroom_id = chatroom_id)
        for chat in chats:
            if chat.read == False:
                chat.read = True
                chat.save()
        user = ChatRoom.objects.get(id = chatroom_id).users.exclude(id = request.user.id)
        detail = True
        context['chat_detail']=chats
        context['user_id']=user[0].id
        
    else:
        detail = False
    context['detail']=detail
    
    return render(request, 'chat/main.html',context)

def send_msg(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            chatroom = ChatRoom.objects.filter(users__id = request.user.id and request.POST.get('user_id')).first()
            if chatroom==None:
                chatroom = ChatRoom()
                if request.POST.get('annonymous')==True:
                    chatroom.annonymous=True
                chatroom.save()
                chatroom.users.add(request.user)
                chatroom.users.add(myUser.objects.get(id = request.POST.get('user_id')))
                chatroom.save()
            
            new_msg = form.save(commit=False)
            new_msg.user = myUser.objects.get(id = request.user.id)
            new_msg.chatroom = chatroom
            new_msg.save()
            
        return redirect(request.POST.get('prv_path'))
    
def msg_detail(request):
    return render(request, "chat/list.html")