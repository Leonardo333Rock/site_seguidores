from django.shortcuts import render


def Home(request):
    return render(request,'home.html')

def Instagram(request):
    return render(request,'redes/instagram.html')
