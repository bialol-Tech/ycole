from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .forms import AuthenticationForm
# Create your views here.


def authentification(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('accueil')  # Redirigez vers la page d'accueil ou une autre page après connexion
    else:
        form = AuthenticationForm()
    return render(request, 'authentification/login.html', {'form': form})