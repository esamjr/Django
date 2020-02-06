from django.shortcuts import render

# Variable
context = {
        'judul':'Welcome To Django Project',
        'subjudul':'~~Rest In Peace Kobe~~',
        'banner' : 'img/banner_home.png',
        'nav':[
            ['/','Home'],
            ['/blog','Blog'],
            ['/about','About'],
            ['/contact','Contact'],
        ]
    }

# Method Views Index

def index(request):
	return render(request,'index.html', context)

def about(request):
    return render(request,'about.html')
