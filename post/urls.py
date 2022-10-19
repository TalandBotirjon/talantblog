from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('<int:id>/', detail, name='detail'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]