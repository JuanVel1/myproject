from django.shortcuts import render

# Create your views here.
from .models import Director, Movie, Meta


def index(request):
    num_directors = Director.objects.all().count()
    num_Movies = Movie.objects.all().count()

    return render(
        request,
        'index.html',
        context={
            'num_directors': num_directors,
            'num_Movies': num_Movies
        }
    )
