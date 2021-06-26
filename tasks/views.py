from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def Ola(request):
    return(HttpResponse('Ola'))

def tasklist(request) :
    return render(request,'tasks/list.html ')

def yourname(request,name) :
    return render(request,'tasks/yourname.html',{'name':name})   
