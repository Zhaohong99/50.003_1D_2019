from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse,HttpResponseForbidden
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages

from input_field_test import Input_field_test

from createuser.models import Extended_User


error_message_success = "Edit profile success"
error_message_empty_input = "Please fill in all input fields"
error_message_invalid_input = "Please ensure input fields are valid"
error_message_one_checkbox = "Please choose to be notified via SMS, email, or both"
error_message_unauthorised = "Not authorised"  # used if the token sent by form does not tally with the one specified in /Source/webs$
error_message_unknown_error = "Unknown error"  # thrown when we cant save ticket into model for some reason

@csrf_exempt
def view_profile(request):
	"""
	For admins and non-admin, allows user to view current email, phone number, notification preferences,
	and can change email, phone number, notiifcation preferences, and password.

	We did not reuse the function in createuser as reusing requires us to pass some parameter to specify that
	we're editing account instaed of creating account. This parameter may potentially be changd which compromises our system.

	"""
	error_message = None

	if request.user.is_authenticated:
		if request.method == 'POST': 
			username_validity = []
			password_validity = []
			email_validity = []
			phonenumber_validity = []
			username = None
			password = None
			email = None
			phonenumber = None
			notify_email = None
			notify_sms = None
			print("PING")

			try:
				username = request.POST.get('username')
				password = request.POST.get('password')
				email = request.POST.get('email')
				phonenumber = request.POST.get('phoneNumber')
				notify_email = request.POST.get('notify_email')
				notify_sms = request.POST.get('notify_sms')
			except ValueError:
				pass

			# testing input field validity
			input_field_test = Input_field_test()
			username_validity = input_field_test.username(username)
			password_validity = input_field_test.password(password)
			email_validity = input_field_test.email(email)
			phonenumber_validity = input_field_test.phonenumber(phonenumber)

			if len(username_validity)==1 and len(email_validity)==1 and len(phonenumber_validity)==1 and "invalid value" not in password_validity:  # note that password input field may be empty. if so, password is not changed
				# input fields are valid
				user = Extended_User.objects.get(id=request.user.id)
				input_notify_email = False
				input_notify_sms = False

				if notify_email == "True":
					input_notify_email = True
				if notify_sms == "True":
					input_notify_sms = True

				if input_notify_sms or input_notify_email:
					user.username = username
					user.email = email
					user.phoneNumber = phonenumber
					user.notify_email = input_notify_email
					user.notify_sms = input_notify_sms

					if "empty" not in password_validity:
						user.set_password(password)
					user.save()
					error_message = error_message_success
				else:
					error_message = error_message_one_checkbox
			else:
				# input fields are not valid
				empty_input_state = False
				invalid_input_state = False

				for i in username_validity:
					if i == "empty":
						empty_input_state = True
					elif i == "invalid value":
						invalid_input_state = True
				for i in password_validity:
					if i == "invalid value":
						invalid_input_state = True
				for i in email_validity:
					if i == "empty":
						empty_input_state = True
					elif i == "invalid value":
						invalid_input_state = True
				for i in phonenumber_validity:
					if i == "empty":
						empty_input_state = True
					elif i == "invalid value":
						invalid_input_state = True

				if empty_input_state:
					# input fields are empty
					error_message = error_message_empty_input
				elif invalid_input_state:
					# input fields have invalid input
					error_message = error_message_invalid_input

			if error_message == error_message_success:
				messages.success(request, error_message)
			else:
				messages.error(request, error_message)

		# applicable for both GET and POST requests
		user_information = {'username':None, 'email':None, 'phoneNumber':None, 'notify_email':None, 'notify_sms':None}

		# extended_user_row = Extended_User.objects.get(id=request.user.id)
		user_information['username'] = request.user.username
		user_information['email'] = request.user.email
		user_information['phoneNumber'] = request.user.phoneNumber
		user_information['notify_email'] = request.user.notify_email
		user_information['notify_sms'] = request.user.notify_sms

		return render(request, 'profile.html', {'error_message':error_message, 'user_information':user_information})
	else:
		return HttpResponseRedirect(reverse("login:index"))


# @csrf_exempt
# def view_profile(request):
#     if (request.user.is_authenticated):
#         email = request.user.email
#         print(email)
#         #phoneNo = request.user.phoneNumber
#         username = request.user.username
#         line = [email,username]
#         return render(request, "Profile/viewProfile.html", {"line": line})
#     else:
#         return HttpResponseRedirect(reverse("login:index"))




def update_profile(request):
    if (request.user.is_authenticated):
        # user is logged in
        if request.method == 'POST':
            username = request.user.username
            email = request.user.email
            phone = request.POST.get('email')
            description = request.POST.get('description')
            print(username)
            ticket = models.Ticket(ticket_id=id, title=title, resolved=0, read=0, description=description, user=username)
            ticket.save()
        return render(request, 'ticketcreation/creation.html')
    else:
        return HttpResponseRedirect(reverse("login:index"))
