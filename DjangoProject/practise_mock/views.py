from django.shortcuts import render,HttpResponse
from .models import MockTest
from django.http import Http404
from django.utils.safestring import SafeString


# Create your views here.
'''
def index(request):
    all_albums = Album.objects.all()
    html =''
    for album in  all_albums:
        url  = '/music/' + str(album.id) +'/'
        html +='<a href="'+ url +'">'+ album.album_title +'</a><br>'
    return HttpResponse(html)
'''
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
