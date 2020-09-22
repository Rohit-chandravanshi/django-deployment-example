from django.shortcuts import render
from django.http import HttpResponse
from Firstapp.models import  Accessrecord,Topic,webpage,user
from Firstapp.forms import NewUserForm



# Create your views here.
def index(request):
    webpagelist = Accessrecord.objects.order_by("date")
    date_dict = {"access_records":webpagelist}


    # mydict = {'insert_me':"Hello!!! I am from views.py"}
    return render(request,'Firstapp/index.html',context=date_dict)
#
def users(request):
    userlist = user.objects.order_by('first_name')
    user_dict = {'users':userlist}
    return render(request,'Firstapp/index2.html',context=user_dict)

def user(request):
    form = NewUserForm()

    if request.method=="POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return index(request)
        else:
            print("ERROR FORM INVALID")
    return render(request,'Firstapp/users.html',{"form":form})


from Firstapp import forms

def form_name_view(request):
    form = forms.FormName()
    if request.method =="POST":
        form = forms.FormName(request.POST)

        if form.is_valid():
            # DO SOMETHING
            print("Validation Success!")
            print("Name: " + form.cleaned_data["name"])
            print("email: " + form.cleaned_data["email"])
            print("text: " + form.cleaned_data["text"])
    return render(request,'Firstapp/forms.html',{'form':form})


def other(request):
    return render(request,'Firstapp/other.html')

def relative(request):
    return render(request,'FIrstapp/relative_url_template.html')

## UserLogon
from Firstapp.forms import UserProfileInfoForm, UserForm

def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES["profile_pic"]
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'Firstapp/registration.html',{
        'user_form':user_form,"profile_form":profile_form,"registered":registered
    })

## Logon
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user  = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active")
        else:
            print("someone tried to login and failed")
            print("username {} and password {}".format(username,password))
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request,'Firstapp/login.html',{})

@login_required
def special(request):
    return HttpResponse("You are logged in!")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))







