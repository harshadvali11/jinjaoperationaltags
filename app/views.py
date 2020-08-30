from django.shortcuts import render

# Create your views here.

def h1(request):
    d={'name':'Baba Chari'}
    return render(request,'h1.html',d)# giving context is optional

def h2(request):
    return render(request,'h2.html')


def h3(request):
    return render(request,'h3.html')

def h4(request):
    return render(request,'h4.html',context={'a':10000,'b':1000})



