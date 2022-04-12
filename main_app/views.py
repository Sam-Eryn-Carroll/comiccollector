from sre_constants import SUCCESS
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Comic



def home(request):
    return HttpResponse('<h1>Hello</H1>')

def about(request):
    return render(request, 'about.html')

def comics_index(request):
    comics = Comic.objects.all()
    return render(request, 'comics/index.html', { 'comics': comics})

def comics_detail(request, comic_id):
    comic = Comic.objects.get(id=comic_id)
    return render(request, 'comics/detail.html', { 'comic': comic})

class ComicCreate(CreateView):
    model = Comic
    fields = '__all__'

class ComicUpdate(UpdateView):
    model = Comic
    fields = '__all__'

class ComicDelete(DeleteView):
    model = Comic
    success_url = '/comics/'