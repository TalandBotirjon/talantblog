from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>/', views.detail, name='detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]