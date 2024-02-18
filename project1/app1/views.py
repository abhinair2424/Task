from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Person

# Create your views here.
def fn1(request):
    return HttpResponse("Hai")

def form(request):
    return render(request,"form.html")


# def arithmetics(request):
#     N1 = int(request.GET['num1'])
#     N2 = int(request.GET['num2'])
#     add = N1+N2
#     subs = N1-N2
#     mul = N1*N2
#     div = N1/N2
#     res = {'Addition':add,
#            'Subtraction':subs,
#            'Multiplication': mul,
#            'Division': div
#            }
#     return render(request,"result.html",res)

def travel(request):

    obj=Place.objects.all()
    obj2=Person.objects.all()
    return render(request,"index.html",{'result':obj,'result2':obj2})




