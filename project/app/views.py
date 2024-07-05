from django.shortcuts import render
from .models import *


# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def courses(request):
    return render(request, "courses.html")


def login(request):
    return render(request, "login.html")


def playlist(request):
    return render(request, "playlist.html")


def profile(request):
    return render(request, "profile.html")


def register(request):
    return render(request, "register.html")


def teacher_profile(request):
    return render(request, "teacher_profile.html")


def teachers(request):
    return render(request, "teachers.html")


def update(request):
    return render(request, "update.html")


def watch_video(request):
    return render(request, "watch-video.html")



# User Registration
def user_register(request):
    if request.method == "POST":
        Name = request.POST.get("name")
        Email = request.POST.get("email")
        Password = request.POST.get("pass")
        Cpassword = request.POST.get("c_pass")
        Profile = request.FILES.get("profile")
        user = Userregister.objects.filter(Email=Email)

        if user:
            message = "User already exist"
            return render(request, "register.html", {"msg": message})
        else:
            if Password == Cpassword:
                user = Userregister(
                    Name=Name,
                    Email=Email,
                    Password=Password,
                    Cpassword=Cpassword,
                    Profile=Profile,
                )
                user.save()
                message = "User register Successfully"
                return render(request, "login.html", {"msg": message})
            else:
                message = "Password not match"
                return render(request, "register.html", {"msg": message})


# User Login
def userLogin(request):
    if request.method == "POST":
        Email = request.POST.get("email")
        Password = request.POST.get("pass")
        user = Userregister.objects.filter(Email=Email)
        if user:
            data = Userregister.objects.get(Email=Email)
            if data.Password == Password:
                Name = data.Name
                Email = data.Email
                Profile=data.Profile
                user={
                    'Name':Name,
                    'Email':Email,
                    'Profile':Profile
                }
                return render(request,"profile.html",user)
            else:
                message = "Password not match"
                return render(request, "login.html", {"msg": message})
        else:
            message = "User not exist"
            return render(request, "register.html", {"msg": message})
