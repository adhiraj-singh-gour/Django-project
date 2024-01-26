from django.urls import path,include
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('courses/',courses,name='courses'),
    path('login/',login,name='loginpage'),
    path('playlist/',playlist,name='playlist'),
    path('profile/',profile,name='profile'),
    path('register/',register,name='registerpage'),
    path('teacher_profile/',teacher_profile,name='teacher_profile'),
    path('teachers/',teachers,name='teachers'),
    path('update/',update,name='update'),
    path('watch_video/',watch_video,name='watch-video'),

    # User Registration
    path('user_register/',user_register,name='user_register'),
    path('userLogin',userLogin,name='userLogin'),
]
