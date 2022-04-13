from email import charset
from sre_constants import SUCCESS
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Comic, Character
from .forms import ReviewForm



def home(request):
    return HttpResponse('<h1>Hello</H1>')

def about(request):
    return render(request, 'about.html')

def comics_index(request):
    comics = Comic.objects.all()
    return render(request, 'comics/index.html', { 'comics': comics})

def comics_detail(request, comic_id):
    comic = Comic.objects.get(id=comic_id)
    id_list = comic.characters.all().values_list('id')
    characters_comic_dosent_have = Character.objects.exclude(id__in=id_list)
    review_form = ReviewForm()
    return render(request, 'comics/detail.html', { 
        'comic': comic,
        'review_form': review_form,
        'characters': characters_comic_dosent_have
         })

def assoc_character(request, comic_id, character_id):
    Comic.objects.get(id=comic_id).characters.add(character_id)
    return redirect('detail', comic_id=comic_id)

class ComicCreate(CreateView):
    model = Comic
    fields = ['title', 'series', 'issuenumber', 'summary', 'releasedate', 'publisher']

class ComicUpdate(UpdateView):
    model = Comic
    fields = '__all__'

class ComicDelete(DeleteView):
    model = Comic
    success_url = '/comics/'

def add_review(request, comic_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.comic_id = comic_id
        new_review.save()
    return redirect('detail', comic_id=comic_id)

class CharacterList(ListView):
    model = Character

class CharacterDetail(DetailView):
    model = Character

class CharacterCreate(CreateView):
    model = Character
    fields = '__all__'

class CharacterUpdate(UpdateView):
    model = Character
    fields = ['name', 'power']

class CharacterDelete(DeleteView):
    model = Character
    success_url = '/characters/'