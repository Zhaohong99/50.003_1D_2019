from django.http import HttpResponse
from django.shortcuts import render
from . import models
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages



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
        messages.add_message(request, messages.SUCCESS, 'Create Successful')
    return render(request, 'ticketcreation/creation.html')


def list(request):
    list = models.Ticket.objects.all()

    return render(request, 'ticketcreation/show.html', {"list": list})


def detail(request):
    id = request.GET.get("id")
    try:
        models.Ticket.objects.filter(id=id).update(read=1)
        item = models.Ticket.objects.all().filter(id=id)

    except:
        raise HttpResponse(0)
    return render(request, 'ticketcreation/detail.html', {"item": item[0]})

def delete(request):
    print("here!!!!!")
    column_id = request.GET.get("id")
    print(column_id)
    line = models.Ticket.objects.filter(id=column_id).delete()
    list = models.Ticket.objects.all()
    return render(request, 'ticketcreation/show.html', {"list": list})


