from django.shortcuts import render, get_object_or_404, redirect
from .models import bookedMovie, Movie
from .forms import NewMovieForm, EditMovieForm, bookedMovieForm, updateBookedMovie
# Create your views here.

def movies(request):
  movies = Movie.objects.all().values()

  context = {
    'movies':movies
    }
  return render(request, 'movie/movies.html', context)

def movieOne(request, id):
  movie = Movie.objects.get(id=id)

  context = {
    'movie':movie
  }
  return render(request, 'movie/movie.html', context)



def newMovie(request):
    if request.method == 'POST':
        form = NewMovieForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            item.save()

            return redirect('movies')
    else:
        form = NewMovieForm()

    return render(request, 'movie/movie-create-form.html', {
        'form': form,
    })

def bookMovie(request):
    if request.method == 'POST':
        form = bookedMovieForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            item.save()

            return redirect('movies')
    else:
        form = NewMovieForm()

    return render(request, 'movie/movie-create-form.html', {
        'form': form,
    })

def editMovie(request, pk):
    item = get_object_or_404(Movie, pk=pk)

    if request.method == 'POST':
        form = EditMovieForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('movie')
    else:
        form = EditMovieForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
    })