from django.shortcuts import render
from .forms import regist, usr_login
from django.contrib import messages

def login(request):
    form=usr_login(request.POST)
    if request.method=='POST':
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request,'Connexion réussie')
        else:
            usr_login()
    return render(request,'auth/login.html', {'form':form})

def register(request):
    form= regist(request.POST)
    if request.method=='POST':
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request,'Enregistrement réussi')
        else:
            regist()
    return render(request,'auth/register.html', {'form':form})
