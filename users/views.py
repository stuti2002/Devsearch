from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile


# Create your views here.
def loginUser(request):

    if request.user.is_authenticated:
        return redirect("Profiles")
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    
        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request, "username does not exist")
    
        user =  authenticate(request, username=username , password=password)

        if user is not None:
            login(request,user)
            return redirect('Profiles')
        else:
            messages.error(request,"username or password is incorrect")

    return render(request,'users/login_user.html')

def logoutUser(request):
    logout(request)
    messages.error(request, "user is successfully loggedout")
    return redirect('login')


def Profiles(request):
    profiles=Profile.objects.all()
    context={'profiles':profiles}
    return render(request ,'users/profiles.html',context)

def userProfile(request,pk):
    return render(request,'users/user-profile.html')