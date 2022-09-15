
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views
from account import views as account_view
from clothe import views as clothe_view
from post import views as post_view
from chat import views as chat_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',account_view.load),
    path('crawling/',account_view.load_img,name = 'crawling'),
    path('home/',account_view.home,name = 'home'),
    path('login/', auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),
    path('forgot_passward/', account_view.forgot_password,name='forgot_password'),
    path('register/',account_view.register,name='register'),
    path('search/',clothe_view.search,name='search'),
    path('clothe/add',clothe_view.add,name='add_clothe'),
    path('clothe/view/<str:view_for>',clothe_view.list,name = "clothe_view"),
    path('clothe/detail/<str:clothe_id>',clothe_view.detail,name = "clothe_detail"),
    path('community/main',post_view.main,name = 'community_main'),
    path('community/my/<str:type>/',post_view.my_post,name = 'my_post'),
    path('community/<str:type>/',post_view.boards,name = 'boards'),
    path('increase_like/',post_view.increase_like, name = 'increase_like'),
    path('new_post/<str:type>/',post_view.postFormInput,name = 'new_post'),
    path('add_post/<str:type>/',post_view.add,name = 'add_post'),
    path('community/<str:type>/<str:post_id>/',post_view.detail,name = 'post_detail'),
    path('mylooks/',clothe_view.mylooks,name = 'mylooks'),
    path('community/new_post',post_view.add,name = 'new_post'),
    path('favorites/',clothe_view.favorite,name = 'favorite'),
    path('weather/',clothe_view.weather,name = 'weather'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('mypage/',account_view.setting,name = 'settings'),
    path('chattings/<str:chatroom_id>',chat_view.chatting,name = "chattings"),
    path('send_msg/',chat_view.send_msg,name = "send_msg"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

