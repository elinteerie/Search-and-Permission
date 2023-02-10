from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Movies

# Create your views here.


def movie_list(request):
    movie_objects = Movies.objects.all()

    movie_name = request.GET.get('movie_name')
    if movie_name != '' and movie_name is not None:
        movie_objects = movie_objects.filter(name__icontains=movie_name)

    paginator = Paginator(movie_objects, 5)
    page = request.GET.get('page')
    movie_objects = paginator.get_page(page)
    context = {'movie_objects': movie_objects}
    return render(request, 'newapp/movie_list.html', context=context)
