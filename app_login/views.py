from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from app_login import forms

# Create your views here.
def SingUp(request):
    form = forms.UserInfoform()
    registered = False
    if request.method == 'POST':
        form = forms.UserInfoform(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True
    dict = {
        'form':form,
        'registered':registered
    }
    return render(request, 'app_login/singup.html', context=dict)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            
    else:
        form = AuthenticationForm()
            
    return render(request, 'app_login/login.html', context={'form':form})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def profile(request):
    return render(request, 'app_login/profile.html', context={})

@login_required
def ProfileChang(request):
    current_user = request.user
    form = forms.UserChangeInfo(instance=current_user)
    if request.method == 'POST':
        form = forms.UserChangeForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = forms.UserChangeForm(request.POST, instance=current_user)
    return render(request, 'app_login/profile_change.html', context={'form':form})



@login_required
def pass_change(request):
    curren_user = request.user
    changed = False
    form = PasswordChangeForm(curren_user)
    if request.method == 'POST':
        form = PasswordChangeForm(curren_user, data=request.POST)
        if form.is_valid():
            form.save()
            changed = True

    return render(request, 'app_login/pass_change.html', context={'form':form, 'changed':changed})

@login_required
def Profile_pic_add(request):
    form = forms.Profile_pic_add()
    if request.method == 'POST':
        form = forms.Profile_pic_add(request.POST, request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('app_login:profile'))
    return render(request, 'app_login/pro_pic_add.html', context={'form':form})


@login_required
def Change_Profile(request):
    form = forms.Profile_pic_add(instance=request.user.user_profile)
    if request.method == 'POST':
        form = forms.Profile_pic_add(request.POST, request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('app_login:profile'))
    return render(request, 'app_login/pro_pic_add.html', context={'form':form})