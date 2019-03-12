from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout

from .forms import UserForm


@csrf_exempt
def get_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        id = request.POST.get('id')
        email = request.POST.get('email')
        phoneNumber = request.POST.get('phoneNumber')

        user=User.objects.filter(username=username)
        print(type(user))

        if user.exists()==False:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.is_active = True
            user.save()
            print("success")
            print(user.password)
            return HttpResponseRedirect('/login/')
        else:
            HttpResponse("User Exist")
            #this = User.objects.get(username=username)
            #print(this.password)


    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()

    return render(request, 'createuser/user.html')
