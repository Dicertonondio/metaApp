from django.urls import path
from . import views


urlpatterns = [
    path('', views.ticket, name='ticket'),
    path('add/', views.add_ticket, name='add_ticket'),
    path('<int:ticket_id>/', views.edit_ticket, name='edit_ticket'),
    path('<int:ticket_id>/delete/', views.delete_ticket, name='delete_ticket'),
    path('<int:ticket_id>', views.ticket_by_id, name='ticket_by_id'),
    path('your_ticket', views.your_ticket, name='your_ticket'),
]