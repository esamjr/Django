from django.shortcuts import render
# Create your views here.
context = {
        'judul':'About Page',
        'nav':[
            ['/','Home'],
            ['/blog','Blog'],
            ['/about','About'],
            ['/contact','Contact'],
        ]
    }


def index(request):
    return render(request,'index.html', context)

