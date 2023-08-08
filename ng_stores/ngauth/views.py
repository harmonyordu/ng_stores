from django.shortcuts import render, redirect

def signup(request):
    return render(request, "ngauth/signup.html")

def handlelogin(request):
    return render(request, "ngauth/login.html")

def handlelogout(request):
    return redirect("/ngauth/login.html")

