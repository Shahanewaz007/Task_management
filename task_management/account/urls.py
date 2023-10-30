from django.urls import path
from .views import register, user_login,user_logout, user_profile,change_password

urlpatterns = [
    path('register/', register , name='register'),
    path('login/', user_login , name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/<int:id>/', user_profile, name='profile'),
    path('change_password/', change_password, name='change_password'),
]