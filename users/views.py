from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import CustomUserCreationForm


# Create your views here.
def loginUser(request):
    print("login userfunction call")
    
    if request.user.is_authenticated:
        return redirect('Profiles')
    print("user is authenticated")
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        try:
            user=User.objects.get(username=username)
            print(user)
        except:
            messages.error(request, "username does not exist")
    
        user =  authenticate(request, username=username , password=password)

        if user is not None:
            login(request,user)
            print("login successfull")
            return redirect('Profiles')
        else:
            print("else....")
            messages.error(request,"username or password is incorrect")
    print("nothing ")
    return render(request,'users/login_user.html')

def logoutUser(request):
    logout(request)
    messages.success(request, "user is successfully loggedout")
    return redirect('login')

def registerUser(request):
    page='register'
    form=CustomUserCreationForm()
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username= user.username.lower()
            user.save()
            messages.success(request,"User acount is created")
        
            login(request,user)
            return redirect('login')
        else:
            messages.error(request,"Error occured while creation....")



    context={'page':page , 'form':form}
    return render(request,'users/login_user.html',context)


def Profiles(request):
    profiles=Profile.objects.all()
    context={'profiles':profiles}
    return render(request ,'users/profiles.html',context)

def userProfile(request,pk):
    profile=Profile.objects.get(id=pk)
    topskills=profile.skill_set.exclude(description__exact="")
    otherskills=profile.skill_set.filter(description="")
    context={'profile':profile,'topskills':topskills,'otherskills':otherskills}
    return render(request,'users/user-profile.html',context)