from django.shortcuts import render
from . import models
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def create(request):
    if request.method == 'POST':
        id = 5
        username = request.POST.get("username")
        title = request.POST.get("title")
        print(username)
        email = request.POST.get('email')
        description = request.POST.get('description')
        print(username)
        ticket = models.Ticket(ticket_id=id, title=title, resolved=0, read=0, description=description, user=username)
        ticket.save()

    return render(request, 'ticketcreation/creation.html')


def list(request):
    list = models.Ticket.objects.all()

    return render(request, 'ticketcreation/show.html', {"list": list})


def dashboard(request):
    return render(request, 'ticketcreation/Dashboard.html')
