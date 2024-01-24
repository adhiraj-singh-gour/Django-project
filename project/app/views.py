from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')

def courses(request):
    return render(request,'contact.html')

def login(request):
    return render(request,'login.html')

def playlist(request):
    return render(request,'playlist.html')

def profile(request):
    return render(request,'profile.html')

def register(request):
    return render(request,'register.html')

def teacher_profile(request):
    return render(request,'teacher_profile.html')

def teachers(request):
    return render(request,'teachers.html')

def update(request):
    return render(request,'update.html')

def watch_video(request):
    return render(request,'watch-video.html')


