from django.urls import path
from voti.views import view_a,view_b,view_c,view_d

app_name="voti"
urlpatterns=[
    path('view_a/', view_a, name='view_a'),
    path('view_b/', view_b, name='view_b'),
    path('view_c/', view_c, name='view_c'),
    path('view_d/', view_d, name='view_d'),
]