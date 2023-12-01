from django.urls import path
from .views import homenews, articoloDetailView, listaArticoli

app_name = 'news'
urlpatterns = [
    path('articoli/<int:pk>', articoloDetailView, name="articolo_detail"),
    path('', homenews, name="homeview"),
    path('lista_articoli/<int:pk>', listaArticoli, name="lista_articoli_giornalista"),
    path('lista_articoli/', listaArticoli, name="lista_articoli"),
]