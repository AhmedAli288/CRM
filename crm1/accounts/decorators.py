from django.shortcuts import redirect
from django.http import HttpResponse



def unauthorized_user(view_function):
	def wrapped_function(request,*args,**kwargs):

		if request.user.is_authenticated:
			return redirect('home')

		else:
			return view_function(request, *args, **kwargs)

	return wrapped_function



def allowed_users(allow_users = []):
	def decorate(view_function):
		def wrapped_function(request, *args, **kwargs):

			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name

			if group in allow_users:
				return view_function(request, *args, **kwargs)
			else:
				return HttpResponse('You are not authorized.')

		return wrapped_function
	return decorate



def admin_only(view_function):
	def wrapped_function(request, *args, **kwargs):

		group = None

		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'customer':
			return redirect('user-page')

		if group == 'admin':			
			return view_function(request, *args, **kwargs)

	return wrapped_function