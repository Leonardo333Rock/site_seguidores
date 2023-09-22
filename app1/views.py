from django.shortcuts import render


def Home(request):
    return render(request,'home.html')

def Seguidores_instagram(request):
    return render(request,'instagram/seguidores.html')

def Curtida_insta(request):
    return render(request,'instagram/curtidas.html')

def Visualizacao_insta(request):
    return render(request,'instagram/visualizacao_insta.html')
    


