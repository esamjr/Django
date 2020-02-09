# Views blog

from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
    #queryset 
    posts = Post.objects.all()
    context={
    'judul':'Blog Page',
    'subjudul':'Selamat Datang Di Blog Django',
    'Posts':posts,
}
    return render(request,'blog/index.html', context)

