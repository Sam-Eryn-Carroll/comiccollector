from sre_constants import SUCCESS
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Comic
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
    review_form = ReviewForm()
    return render(request, 'comics/detail.html', { 'comic': comic, 'review_form': review_form})

def add_review(request, comic_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.comic_id = comic_id
        new_review.save()
    return redirect('detail', comic_id=comic_id)

class ComicCreate(CreateView):
    model = Comic
    fields = '__all__'

class ComicUpdate(UpdateView):
    model = Comic
    fields = '__all__'

class ComicDelete(DeleteView):
    model = Comic
    success_url = '/comics/'