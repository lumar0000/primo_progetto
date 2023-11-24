from django.urls import path
from .views import homenews, articoloDetailView

app_name = 'news'
urlpatterns = [
    path('articoli/<int:pk>', articoloDetailView, name="articolo_detail"),
    path('', homenews, name="homeview"),
   
]