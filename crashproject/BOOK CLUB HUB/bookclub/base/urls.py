from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('', views.home, name='home'),
    path('club/<str:pk>', views.club, name='club'),
    path('create-club', views.createClub, name='create-club'),
    path('update-club<str:pk>', views.updateClub, name='update-club'),
    path('delete-club<str:pk>', views.deleteClub, name='delete-club'),
]