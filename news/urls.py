from django.urls import path
from .views import homenews, articoloDetailView, listaArticoli, queryBase, giornalisti_list_api, giornalisti_api, articoli_list_api, articoli_api

app_name = 'news'
urlpatterns = [
    path('articoli/<int:pk>', articoloDetailView, name="articolo_detail"),
    path('', homenews, name="homeview"),
    path('lista_articoli/<int:pk>', listaArticoli, name="lista_articoli_giornalista"),
    path('lista_articoli/', listaArticoli, name="lista_articoli"),
    path('query_base/', queryBase, name="query_base"),
    
    path('giornalisti_list_api/', giornalisti_list_api, name="giornalisti_list_api"),
    path('giornalisti_api/<int:pk>', giornalisti_api, name="giornalisti_api"),
    path('articoli_list_api/', articoli_list_api, name="articoli_list_api"),
    path('articoli_api/<int:pk>', articoli_api, name="articoli_api"),
]