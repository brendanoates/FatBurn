from django.shortcuts import render

__author__ = 'boates'
from django.http import HttpResponse
from django.views.generic import View
class Home(View):
    def get(self, request):
        context = {'title':'Home Page'}
        return render(request, 'fatburn/home.html',context)

class StartTheBurn(View):
    def get(self, request):
        context = {'title':'Start The Burn'}
        return render(request, 'fatburn/startTheBurn.html',context)

class About(View):
    def get(self, request):
        context = {'title':'About'}
        return render(request, 'fatburn/about.html',context)