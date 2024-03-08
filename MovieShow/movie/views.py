from django.shortcuts import render, get_object_or_404, redirect
from .models import bookedMovie, MovieDetails
from .forms import NewMovieForm, EditMovieForm
from  django.contrib.auth.decorators  import  login_required
# Create your views here.

def movies(request):
  movies = MovieDetails.objects.all().values()
  if request.method == 'POST':
      user = request.user,
      description = MovieDetails.description,
      price = MovieDetails.price,
      created_at = MovieDetails.created_at,
      booking = request.POST.get('isBooked')
      
      return redirect('book')
  context = {
    'movies':movies
    }
  return render(request, 'movie/movies.html', context)



def bookMovie(request):
    movie = bookedMovie.objects.filter(booking=True)

    context = {
        'movie': movie,
    }
    return render(request,'movie/booked-movies.html', context )


# @login_required(login_url='/userAuth/login/')
def movieOne(request, id):
  movie = MovieDetails.objects.get(id=id)
 
  context = {
    'movie':movie
  }
  return render(request, 'movie/movie.html', context)


@login_required(login_url= '/login/')
def newMovie(request):
      form = NewMovieForm()
      if request.method == 'POST':
          form = NewMovieForm(request.POST, request.FILES)

          if form.is_valid():
              form.save()

              return redirect('movies')
      else:
          form = NewMovieForm()

      return render(request, 'movie/movie-create-form.html', {
          'form': form,
    })

    
@login_required(login_url= '/login/')
def editMovie(request, pk):
    item = get_object_or_404(MovieDetails, pk=pk)

    if request.method == 'POST':
        form = EditMovieForm(request.POST, instance=item)

        if form.is_valid():
            form.save()

            return redirect('movies')
    else:
        form = EditMovieForm(instance=item)

    return render(request, 'movie/edit-movie-form.html', {
        'form': form,
    })
@login_required(login_url= '/login/')
def deleteMovie(request, id):
    
    movieOne = MovieDetails.objects.get(id=id)
    if request.method == 'POST':
        movieOne.delete()
        return redirect('movies')

    context = {
        'movie': movieOne
    }
    return render(request, 'movie/delete-movie.html', context)

# def bookMovie(request):
#     if request.method == 'POST':
#         form = bookedMovieForm(request.POST)

#         if form.is_valid():
#             item = form.save(commit=False)
#             item.save()

#             return redirect('movies')
#     else:
#         form = NewMovieForm()

#     return render(request, 'movie/movie-create-form.html', {
#         'form': form,
#     })
