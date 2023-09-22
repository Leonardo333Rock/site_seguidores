from django.shortcuts import render


def Home(request):
    return render(request,'home.html')

            #INSTAGRAM

def Seguidores_instagram(request):
    return render(request,'instagram/seguidores.html')

def Curtida_insta(request):
    return render(request,'instagram/curtidas.html')

def Visualizacao_insta(request):
    return render(request,'instagram/visualizacao_insta.html')

            # FACEBOOK
    
def Seguidores_face(request):
    return render(request,'facebook/seguidores_face.html')

def Curtidas_face(request):
    return render(request,'facebook/curtidas_face.html')

def Visualizacao_face(request):
    return render(request,'facebook/visualizacao_face.html')


