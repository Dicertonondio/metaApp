from django.urls import path
from . import views


urlpatterns = [
    path('', views.visualizza_client, name='visualizza_client'),
    path('add/', views.add_client, name='add_client'),
    path('<int:client_id>/', views.edit_client, name='edit_client'),
    path('<int:client_id>/delete/', views.delete_client, name='delete_client'),
    path('<int:client_id>', views.client_by_id, name='client_by_id'),
] 