from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

def signup(request):
    
    if request.method== "POST":
        email= request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password != confirm_password:
            messages.warning(request, 'The password does not match')
            return render(request, 'auth/signup.html')
    
        try:
            if User.objects.get(username=email):
                messages.warning(request,'User already exist')
                return render(request, 'auth/signup.html')
            
        except Exception as identifier:
            pass
        
        user = User.objects.create_user(email,email,password)
        user.save()
        return HttpResponse("User Created", email)  
    return render(request, "authentication/signup.html") 

def handlelogin(request):
    return render(request, "auth/login.html")

def handlelogout(request):
    return redirect("/auth/login.html")

