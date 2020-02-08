from django.shortcuts import render
# Create your views here.
context = {
        'judul':'About Page',
    }


def index(request):
    return render(request,'about/index.html', context)

