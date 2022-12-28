from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def second(request):
    return HttpResponse('APP2 view1')

def h2(request):
    return render(request,'h2.html')