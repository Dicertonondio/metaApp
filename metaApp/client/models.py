from django.contrib.auth.models import User
from django.contrib import admin
from django.db import models

class client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    nome = models.CharField(max_length=50)
    telefono = models.CharField(max_length=12, default='')
    piano = models.CharField(max_length=50,default='')
    indirizzo = models.CharField(max_length=255)
    created_at = models.DateTimeField('created at', auto_now_add=True)
    updated_at = models.DateTimeField('updated at', auto_now=True)

    def __str__(self):
        return self.nome

admin.site.register(client)

