from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('APP1 view1')

def h1(request):
    return render(request,'h1.html')