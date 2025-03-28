from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),

    path('', views.home, name='home'),
    path('club/<str:pk>', views.club, name='club'),

    path('create-club', views.createClub, name='create-club'),
    path('update-club<str:pk>', views.updateClub, name='update-club'),
    path('delete-club<str:pk>', views.deleteClub, name='delete-club'),

    path('delete-message<str:pk>', views.deleteMessage, name='delete-message'),
    path('update-message<str:pk>', views.updateMessage, name='update-message'),
]