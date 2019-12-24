from django.shortcuts import render
from django.http import HttpResponse
from .models import Users

# Create your views here.

def home(request):
	# users = [Users.objects.all()]
	# print ("###########",users[0])
	# return HttpResponse('Hello, World!')
	return render(request, 'home.html', {'boards': "boards"})
