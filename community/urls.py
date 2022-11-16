from django.urls import path
from . import views

urlpatterns = [
    path('', views.com_home, name='c_home'),
    path('add-post/', views.addFeed, name='add-post'),
    path('edit-post/<str:pk>/', views.editFeed, name='edit-post'),
    path('delete-post/<str:pk>/', views.deleteFeed, name='delete-post'),

]
