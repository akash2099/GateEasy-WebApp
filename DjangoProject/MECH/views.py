from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def mechhome(request):
    return render(request, 'mech.html')

def mechcontact(request):
    messages.success(request, 'GateEasy team will contact you soon.')
    return redirect('mechhome')

def mocktest(request):
    return render(request, 'Mock.html')

def videolec(request):
    return render(request, 'video-lec.html')