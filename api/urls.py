from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', views.getRoutes),
    path('profiles/', views.getProfiles),
    path('profiles/<str:pk>/', views.getProfile),
    path('edit-profile/<str:pk>/', views.editProfile),

    path('inbox/', views.getInbox),
    path('inbox/<str:pk>/', views.viewMessage),
    path('create-message/', views.createMessage),
    path('delete-message/<str:pk>/', views.deleteMessage),

    path('verify/', views.verifyUsers),
    path('verify/<str:pk>/', views.verifyUser),

]
