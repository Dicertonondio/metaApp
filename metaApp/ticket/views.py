from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Ticket, TicketStatus
from client.models import client
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required


@staff_member_required
def ticket(request):
    tickets = Ticket.objects.order_by('-created_at')
    return render(request,'ticket/ticket.html', {'tickets': tickets})


def your_ticket(request):
    tickets = Ticket.objects.order_by('-created_at')
    return render(request,'ticket/your_ticket.html', {'tickets': tickets})    



def ticket_by_id(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    return render(request, 'ticket/ticket_by_id.html', {'ticket':ticket})



def add_ticket(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        assignee_id = request.POST.get('assignee')
        status_id = TicketStatus.TO_DO  # Imposta lo stato di default su TO_DO
        description = request.POST.get('description')
        status = request.POST.get('status')
        assignee = User.objects.get(id=assignee_id) if assignee_id else None
        ticket = Ticket(title=title, assignee=assignee, status=status, description=description)
        ticket.save()
        return redirect('your_ticket')
    users = User.objects.all()
    status_choices = [(status.name, status.value) for status in TicketStatus]
    context = {'users': users, 'status_choices': status_choices}
    return render(request, 'ticket/add_ticket.html', context)

@staff_member_required
def edit_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        ticket.title = request.POST.get('title')
        assignee_id = request.POST.get('assignee')
        ticket.assignee = User.objects.get(id=assignee_id) if assignee_id else None
        ticket.status = request.POST.get('status')  
        ticket.description = request.POST.get('description')
        ticket.save()
        return redirect('your_ticket')
    users = User.objects.all()
    status_choices = [(status.name, status.value) for status in TicketStatus]
    context = {'ticket': ticket, 'users': users, 'status_choices': status_choices}
    return render(request, 'ticket/edit_ticket.html', context)

@staff_member_required
def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    ticket.delete()
    return redirect('ticket')