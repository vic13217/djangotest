from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from datetime import datetime

import random

def hello(request):
	#return HttpResponse("Hello World")
	return render(request,'hello.html')

def hello1(request,username):
	now = datetime.now()
	return render(request,'hello1.html',locals())


times = 0

def hello2(request,username):
	global times
	times += 1
	global_times = times
	now = datetime.now()
	dicenum1 = random.randint(1,6);
	dicenum2 = random.randint(1,6);
	dicenum3 = random.randint(1,6);
	dict1 = {"dice1":dicenum1,"dice2":dicenum2,"dice3":dicenum3};

	score = random.randint(0,100);

	return render(request,'hello2.html',locals())


def students(request):
	std1 = {"name" : "user1", "sid" : "001", "age" : 18}
	std2 = {"name" : "user2", "sid" : "002", "age" : 20}
	std3 = {"name" : "user3", "sid" : "003", "age" : 22}
	stds = [std1, std2, std3]
	return render(request, 'std.html',locals())