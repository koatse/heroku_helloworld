from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def test(request):
    return HttpResponse("THis is a test page")
