from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from rest_framework.response import Response

from input_field_test import Input_field_test
from login.forms import LoginForm
from django.contrib import messages

error_message_incorrect_userpass = "Login failure, username or password is incorrect"
error_message_empty_input = "Please fill in all input fields"
error_message_invalid_input = "Please ensure input fields are valid"

@csrf_exempt
def index(request):
	if request.method == 'POST':
		try:
			username = Response['username']
			password = Response['password']
			print(username, password)
		except:
			print("error")

	# response = {}
	#
	# error_message = None
	# if request.method == 'POST':
	# 	username = None
	# 	password = None
	# 	username_validity = []
	# 	password_validity = []
	#
	# 	form = LoginForm(request.POST)
	#
	# 	try:
	# 		username = request.POST['username']
	# 		password = request.POST['password']
	# 	except ValueError:
	# 		pass
	#
	# 	# testing input field validity
	# 	input_field_test = Input_field_test()
	# 	username_validity = input_field_test.username(username)
	# 	password_validity = input_field_test.password(password)
	#
	# 	if len(username_validity)==1 and len(password_validity)==1:
	# 		user = authenticate(username=username, password=password)
	# 		if user is not None:
	# 			# login success
	# 			login(request, user)  # saves user's ID in the session
	# 			return HttpResponseRedirect(reverse("home:index"))
	# 		else:
	# 			# login failure
	# 			error_message = error_message_incorrect_userpass
	# 	else:
    #                     # input fields are not valid
    #                     empty_input_state = False
    #                     invalid_input_state = False
	#
    #                     for i in username_validity:
    #                             if i == "empty":
    #                                     empty_input_state = True
    #                             elif i == "invalid value":
    #                                     invalid_input_state = True
    #                     for i in password_validity:
    #                             if i == "empty":
    #                                     empty_input_state = True
    #                             elif i == "invalid value":
    #                                     invalid_input_state = True
	#
    #                     if empty_input_state:
    #                             # input fields are empty
    #                             error_message = error_message_empty_input
    #                     elif invalid_input_state:
    #                             # input fields have invalid input
    #                             error_message = error_message_invalid_input
    #                     else:
    #                             # uncaught error
    #                             return
	#
	# elif request.method == 'GET':
	# 	pass
	#
	# #return render(request, 'login/not_logged_in.html', {'form':LoginForm(), 'error_message':error_message})
	#return TemplateView.as_view(template_name="index.html")
	return render(request, 'index.html')

def log_out(request):
	logout(request)
	return HttpResponseRedirect(reverse('login:index'))
