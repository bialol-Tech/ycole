from django.shortcuts import render,redirect

# Create your views here.


def Accueil(request):
    return render(request, 'index.html')