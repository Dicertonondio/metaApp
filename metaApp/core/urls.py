# core/urls.py
from django.urls import path, include
from django.views.generic.base import TemplateView # new

urlpatterns = [
     path('', TemplateView.as_view(template_name='home.html'), name='home'), # new
     path('ticket/', include("ticket.urls")),
     path('client/', include("client.urls")),
]
