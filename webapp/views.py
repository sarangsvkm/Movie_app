from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movies
from .forms import MoviesForm


# Create your views here.

def main(req):
    obj = Movies.objects.all()
    return render(req, 'index.html', {'object1': obj})


def details(request, mov_id):
    movie = Movies.objects.get(id=mov_id)
    return render(request, 'details.html', {'movie': movie})


def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']

        movie = Movies(name=name, desc=desc, year=year, img=img)
        movie.save()
    return render(request, 'add.html')


# forms.py

def update(request, id):
    movie = Movies.objects.get(id=id)
    form = MoviesForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'movie': movie})


def delete(request,id):
    if request.method=='POST':
        movie= Movies.objects.get(id= id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')