from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(requests):
    # return HttpResponse('hello')
    return render(requests,'hello.html',{'name':'simon'})