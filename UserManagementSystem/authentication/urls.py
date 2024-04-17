from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('users/<int:user_id>/', UserDetailAPIView.as_view(), name='user-detail'),
    
]