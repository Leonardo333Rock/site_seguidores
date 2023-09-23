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

    #YOUTUBE
    path('seguidores_twi',views.Seguidores_twi,name='seguidores_twi'),
    path('curtidas_twi',views.Curtidas_twi,name='curtidas_twi'),
    path('visualizacao_twi',views.Visualizacao_twi,name='visualizacao_twi'),


    #KWAI
    path('seguidores_kwai',views.Seguidores_kwai,name='seguidores_kwai'),
    path('curtidas_kwai',views.Curtidas_kwai,name='curtidas_kwai'),
    path('visualizacao_kwai',views.Visualizacao_kwai,name='visualizacao_kwai'),


]