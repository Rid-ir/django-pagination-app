from django.core import paginator
from django.shortcuts import render
from .models import Movies
from django.core.paginator import Paginator
# Create your views here.

def movie_list(request):
    movies_object = Movies.objects.all()

    paginator = Paginator(movies_object, 4)
    page = request.GET.get('page')
    movies_object = paginator.get_page(page)

    return render(request, 'newapp/movie_list.html', {'movies_object':movies_object})