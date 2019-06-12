from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
# Create your views here.
def ujautok(request):
    autok = Post.objects.all()  #filter#(title__startswith="Opel").order_by('published_date')
    #mitsu = Post.objects.filter(title__startswith="Mitsubishi").order_by('published_date')
    return render(request, 'bpcore/ujautok2.html',{'autok':autok})


def ujautok_detail(request, slug):
#return HttpResponse(slug)
    details = Post.objects.get(slug=slug)
    return render(request,'bpcore/ujautooldal.html',{'ujauto':details})
