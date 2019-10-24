from django.shortcuts import render
from l5_app.forms import UserForm,UserProfileInfoForm

#using django built in functionality for logins,

from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request,"l5_app/index.html")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False
    #form = {'user_form':UserForm(),'profile_form':UserProfileInfoForm()}
    if request.method == "POST":
        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save() #grabbing user_form and saving it DB
            user.set_password(user.password) #Hashing the passowrd using set_password method
            user.save() #and saving the hashed password to DB
            # grabbing profile_form
            profile = profile_form.save(commit=False) #not saving to DB as we get errors with collision tryong th eoverride user
            profile.user = user #onetoone relationsip with user i.e., with user_form,see line 19

            #setting profile_pic
            #saving to DB before a picture is present or not
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic'] #profile_pic is from key defined in models

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'l5_app/registration.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):
    if request.method == "POST":
        # get username and password to authenticate
        username = request.POST.get('username')  # 'username' from name key in input of html in login
        password = request.POST.get('password')  # 'password' from name key in input of html in login

        # authenticate using authenticate func
        # returns an user object if authenticated/ credentials match
        user = authenticate(username=username,password=password)

        if user:  # if user is authentcated
            if user.is_active:  # if user is active
                login(request,user)  # send request to login using login func
                return HttpResponseRedirect(reverse('index'))  # send to index page
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")  # not active
        else:
            print('Someone tried to login and failed')
            print(f"username : {username} and password : {password}")
            return HttpResponse("Invalid login details provided!")
    else:

        return render(request,'l5_app/login.html',{}) # if not post, then just hit login.html


@login_required
def special(request):
    return HttpResponse("You are logged in...from special function")






