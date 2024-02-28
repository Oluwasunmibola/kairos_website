from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus/', views.aboutus_view, name='aboutus'),
    path('teams/', views.team_view, name='team'),
    path('contact/', views.contact_view, name='contact')
]