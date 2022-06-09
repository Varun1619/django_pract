from django.urls import path
from  . import views

urlpatterns = [
    path('', views.index, name  = "index"),
    path('read/', views.read, name = 'read'),
    path('update/<str:pk>/', views.update, name = 'update'),
    path('delete/<str:pk>/', views.delete_data, name = 'delete')
]