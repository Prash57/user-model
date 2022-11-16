from django.urls import path
from . import views

urlpatterns = [
    path('', views.soc_home , name='')
]