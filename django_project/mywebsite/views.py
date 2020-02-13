from django.shortcuts import render

# Variable
context = {
        'judul':'Welcome To Django Project',
        'subjudul':'~~Rest In Peace Kobe~~',
        'banner' : 'img/banner_home.png',
    }
# Method Views Index
def index(request):
    if request.method == 'POST':
        print("INI Method POST")
        print(request.POST['username'])
        print(request.POST['address'])
    else:
        print("ini Method Get")
    return render(request,'index.html', context)
