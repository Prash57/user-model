from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('login/', views.loginUser, name='login'),
    path('register/', views.registerUser, name='register'),
    path('logout/', views.logoutUser, name='logout'),

    path('profiles/', views.profiles, name='profiles'),
    path('profile/<str:pk>/', views.userProfile, name='profile'),
    path('account/', views.account, name='account'),
    path('edit-account/', views.editAccount, name='edit-account'),
    path('delete-profile/<str:pk>/', views.deleteProfile, name='delete-profile'),

    path('inbox/', views.inbox, name='inbox'),
    path('message/<str:pk>/', views.viewMessage, name='message'),
    path('create-message/<str:pk>/', views.createMessage, name='create-message'),

    path('verify/', views.verifyUser, name='verify')
]
