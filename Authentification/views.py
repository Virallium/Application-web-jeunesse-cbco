from django.shortcuts import render, redirect
from .forms import regist, usr_login
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login as auth_login

def login(request):
    if request.method == 'POST':
        form = usr_login(request.POST)
        
        if form.is_valid():
            # 1. On récupère les données propres saisies dans le formulaire
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            # 2. On vérifie si l'utilisateur existe avec ce mot de passe
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                # 3. Si l'utilisateur est valide, on le connecte
                auth_login(request, user)
                messages.success(request, 'Connexion réussie. Ravis de vous revoir !')
                return redirect('accueil')  # Modifie par le nom de ta route de redirection
            else:
                # Si authenticate renvoie None, les identifiants sont faux
                messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
        else:
            messages.error(request, "Veuillez corriger les erreurs dans le formulaire.")
    else:
        # Requête GET : premier chargement de la page
        form = usr_login()
        
    return render(request, 'auth/login.html', {'form': form})
def register(request):
    form= regist(request.POST)
    if request.method=='POST':
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request,'Enregistrement réussi')
            return redirect('login')
        else:
            regist()
            messages.error(request,"le formulaire n'est pas valide")
    return render(request,'auth/register.html', {'form':form})

def logout_view(request):
   if request.method == "POST":
       logout(request)
       messages.success(request,'Deconnexion reussie')
       return redirect('login')
   return redirect('accueil')
        
