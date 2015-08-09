from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from .models import MP_Success

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()
	
	mp_success = MP_Success()
	
	mp_success_objects = MP_Success.objects.all()
	
    return render(request, 'db.html', {'greetings': greetings})

