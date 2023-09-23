from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='home'),

    #INTAGRAM
    path('seguidores_instagram',views.Seguidores_instagram,name='seguidores_instagram'),
    path('curtidas_instagram',views.Curtida_insta,name='curtidas_instagram'),
    path('visualizacao_insta',views.Visualizacao_insta,name='visualizacao_insta'),

    #FACEBOOK
    path('seguidores_face',views.Seguidores_face,name='seguidores_face'),
    path('curtidas_face',views.Curtidas_face,name='curtidas_face'),
    path('visualizacao_face',views.Visualizacao_face,name='visualizacao_face'),


    #TIKTOK
    path('seguidores_tik',views.Seguidores_tik,name='seguidores_tik'),
    path('curtidas_tik',views.Curtidas_tik,name='curtidas_face'),
    path('visualizacao_tik',views.Visualizacao_tik,name='visualizacao_tik'),

    #YOUTUBE
    path('seguidores_you',views.Seguidores_you,name='seguidores_you'),
    path('curtidas_you',views.Curtidas_you,name='curtidas_you'),
    path('visualizacao_you',views.Visualizacao_you,name='visualizacao_you'),



]