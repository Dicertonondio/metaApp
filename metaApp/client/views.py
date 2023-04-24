from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import client

def visualizza_client(request):
    cliente = client.objects.order_by('-created_at')[:5]
    return render(request, 'client/client.html', {'cliente': cliente})

def add_client(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefono = request.POST.get('telefono')
        piano = request.POST.get('piano')
        indirizzo = request.POST.get('indirizzo')
        cliente = client(nome=nome, telefono=telefono, indirizzo=indirizzo, piano=piano)
        try:
            cliente.save()
        except Exception as e:
            print(e)
        return redirect('visualizza_client')
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'client/add_client.html', context)

def edit_client(request, client_id):
    cliente = client.objects.get(id=client_id)
    if request.method == 'POST':
        cliente.nome = request.POST.get('nome')
        cliente.telefono = request.POST.get('telefono')
        cliente.piano = request.POST.get('piano')
        cliente.indirizzo = request.POST.get('indirizzo')
        cliente.save()
        return redirect('visualizza_client')
    users = User.objects.all()
    context = {'cliente': cliente, 'users': users}
    return render(request, 'client/edit_client.html', context)

def client_by_id(request, client_id):
    cliente = client.objects.get(pk=client_id)
    return render(request, 'client/client_by_id.html', {'cliente':cliente})

def delete_client(request, client_id):
    cliente = get_object_or_404(client, id=client_id)
    cliente.delete()
    return redirect('client')