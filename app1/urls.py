from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('seguidores_instagram',views.Seguidores_instagram,name='seguidores_instagram'),
    path('curtidas_instagram',views.Curtida_insta,name='curtidas_instagram'),
    path('visualizacao_insta',views.Visualizacao_insta,name='visualizacao_insta'),

    path('seguidores_face',views.Seguidores_face,name='seguidores_face'),
    path('curtidas_face',views.Curtidas_face,name='curtidas_face'),
    path('visualizacao_face',views.Visualizacao_face,name='visualizacao_face'),



]