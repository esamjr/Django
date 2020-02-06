from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
context = {
        'judul':'Welcome to About Page || Web Pages Django ',
        'subjudul':'Welome To my Django Project Website',
        'banner' : 'img/banner_about.png',
        'nav':[
            ['/','Home'],
            ['/blog','Blog'],
            ['/about','About'],
            ['/contact','Contact'],
        ]
    }


def index(request):
    return render(request,'about.html', context)

def page1(request):
    return HttpResponse('<h1>Ini About page</h1>')

