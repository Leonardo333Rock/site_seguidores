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


    #TIKTOK

def Seguidores_tik(request):
    return render(request,'tiktok/seguidores_tik.html')

def Curtidas_tik(request):
    return render(request,'tiktok/curtidas_tik.html')

def Visualizacao_tik(request):
    return render(request,'tiktok/visualizacao_tik.html')

    #YOUTUBE

def Seguidores_you(request):
    return render(request,'youtube/seguidores_you.html')

def Curtidas_you(request):
    return render(request,'youtube/curtidas_you.html')

def Visualizacao_you(request):
    return render(request,'youtube/visualizacao_you.html')


    #YOUTUBE

def Seguidores_twi(request):
    return render(request,'twitter/seguidores_twi.html')

def Curtidas_twi(request):
    return render(request,'twitter/curtidas_twi.html')

def Visualizacao_twi(request):
    return render(request,'twitter/visualizacao_twi.html')


    #KWAI

def Seguidores_kwai(request):
    return render(request,'kwai/seguidores_kwai.html')

def Curtidas_kwai(request):
    return render(request,'kwai/curtidas_kwai.html')

def Visualizacao_kwai(request):
    return render(request,'kwai/visualizacao_kwai.html')
