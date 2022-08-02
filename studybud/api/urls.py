from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('users/', views.getUsers, name='users'),
    path('users/<str:pk>/', views.getUser),
    path('create-user/', views.createUser),
    path('update-user/<str:pk>/', views.updateUser),
    path('delete-user/<str:pk>/', views.deleteUser),
    path('rooms/', views.getRooms, name='rooms'),
    path('rooms/<str:pk>/', views.getRoom),
    path('create-room/', views.createRoom),
    path('delete-room/<str:pk>/', views.deleteRoom)

]