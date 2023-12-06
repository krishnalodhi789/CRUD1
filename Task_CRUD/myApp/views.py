from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'home.html')

def userSignup(request):
    if request.method == "POST":
        username=request.POST.get("username")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        conform_password=request.POST.get("conform_password")
        if password == conform_password :
            user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
            user.save()
            messages.success(request, "You have successfully Signup...")
            return redirect("home")
        else:
            messages.error(request, "Password and Conform password are not matched !!")
            return redirect("userSignup")
            
    return render(request,'signupPage.html')


def userLogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            messages.success(request, " You have successfully Loggined")
            return redirect("userProfile")
        else:
            messages.error(request, " Invalid Username and Password !!")
            return redirect("userLogin")
    return render(request, 'loginPage.html')

def userLogout(request):
    logout(request)
    messages.success(request, "You have successfully logout!!")
    return redirect('home')


@login_required(login_url='userLogin')
def userProfile(request):
    return render(request, 'userProfile.html')    



@login_required(login_url='userLogin')
def updateProfile(request):
    if request.method=="POST":
        user = request.user
        user.username=request.POST.get("username")
        user.first_name=request.POST.get("first_name")
        user.email=request.POST.get("email")
        user.save()
        return redirect("userProfile")
    return render(request, 'updateProfile.html')    



def resetPassword1(request):
    if request.method=="POST":
        username=request.POST.get("username")
        user = User.objects.filter(username=username)
        if user.exists():
            return render(request, 'resetPassword2.html',{'username':username})
        else:
            messages.error(request, "Invalid Username")
            return redirect('resetPassword1')           
    return render(request, 'resetPassword1.html')    


def resetPassword2(request):
    if request.method=="POST":
        username=request.POST.get("username")
        user = User.objects.get(username=username)
        password=request.POST.get("password")
        conform_password=request.POST.get("conform_password")
        if password == conform_password :
            user.set_password(password)
            user.save()
            messages.success(request, "You have successfully reset your password.")
            return redirect("userLogin")
        else:
            messages.warning(request, "Password and Conform password are not matched.")
            return render(request, 'resetPassword2.html',{'username':username})
        
    return render(request, 'resetPassword2.html')    

