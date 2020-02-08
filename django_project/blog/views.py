# Views blog

from django.shortcuts import render

# Variable
context={
    'judul':'Blog Page',
    'nav': [
        ['/','Home'],
        ['/blog/cerita','Cerita Blog'],
        ['/blog/news','News'],
        ['/about','About']
    ]
}
# Create your views here.

def index(request):
    return render(request,'blog/index.html', context)

