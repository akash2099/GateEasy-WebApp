from django.shortcuts import render,HttpResponse, get_object_or_404
from .models import MockTest
from django.http import Http404
from django.utils.safestring import SafeString
import json

# Create your views here.

def index(request):
    all_albums = MockTest.objects.all()
    context = {
        'all_albums' : all_albums,
    }
    return render(request,'mock_test.html',context)

def details(request, album_id):
    try:
        mockt = MockTest.objects.get(pk=album_id)
    except MockTest.DoesNotExist:
        raise Http404("MockTest Does not exist")
    return render(request,'mock.html',{'mock' : SafeString(mockt.mock),'info': mockt})

def result(request, album_id):
    album = get_object_or_404(MockTest, pk=album_id)
    if request.method =='POST':
        post_data=json.loads(request.body)
        album.opt_answer= post_data
        album.save()
        
    try:
        mockt = MockTest.objects.get(pk=album_id)
    except MockTest.DoesNotExist:
        raise Http404("MockTest Does not exist")
    return render(request,'mock_result.html',{'mock' : SafeString(mockt.mock),'info': SafeString(mockt.opt_answer['save']), 'obj' : mockt})


   
