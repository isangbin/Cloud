from django.shortcuts import render, redirect
from .models import Movie, Genre
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
import operator, random
# import requests
# import json

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        movies = Movie.objects.all()
        User = get_user_model()
        user = User.objects.get(pk=request.user.pk)
        pickedmovies = user.like_movies.all()

        genre_ids = {28: 0, 12: 0, 16: 0, 35: 0, 80: 0, 99: 0, 18: 0, 10751: 0, 14: 0, 36: 0, 27: 0, 10402: 0, 9648: 0, 10749: 0, 878: 0, 10770: 0, 53: 0, 10752: 0, 37: 0}
        
        for pickedmovie in pickedmovies:
            for genre in pickedmovie.genres.all():
                genre_ids[genre.id] += 1
        
        max_genre = max(genre_ids, key=genre_ids.get)

        if pickedmovies:
            user.favorite = max_genre
        else:
            user.favorite = 0
        user.save()

        # recommends = Movie.objects.filter(genres__contains=max_genre)
        recommends = []

        for movie in movies:
            for genre in movie.genres.all():
                if max_genre == genre.id:
                    recommends.append(movie)
                    break
        
        if pickedmovies:
            recommends = random.sample(recommends, 12)
        else:
            recommends = []
        
        randommovies = list(movies)
        randommovies = random.sample(randommovies, 12)

        context = {
            'movies': movies,
            'pickedmovies': pickedmovies,
            'genre_ids': genre_ids,
            'max_genre': max_genre,
            'recommends': recommends,
            'randommovies': randommovies,
        }
        return render(request, 'movies/index.html', context)
    return redirect('accounts:login')


# def detail(request, movie_pk):
#     movie = Movie.objects.get(pk=movie_pk)
#     context = {
#         'movie': movie,
#     }
#     return render(request, 'movies/detail.html', context)


def detail(request, movie_pk):
    context = {
        'movie_pk': movie_pk,
    }
    return render(request, 'movies/detail.html', context)


@login_required
def select(request):
    movies = Movie.objects.all().order_by('-popularity')[:40]
    context = {
        'movies': movies,
    }
    return render(request, 'movies/select.html', context)


@require_POST
def likes(request, movie_pk):
    if request.user.is_authenticated:
        movie = Movie.objects.get(pk=movie_pk)

        if movie.like_users.filter(pk=request.user.pk).exists():
            movie.like_users.remove(request.user)
            is_liked = False
        else:
            movie.like_users.add(request.user)
            is_liked = True
        context = {
            'is_liked': is_liked,
        }
        return JsonResponse(context)
    return redirect('accounts:login')


def search(request):
    if request.method=='GET':
        searched = request.GET.get("movie")
        searched_type = request.GET.get("type")
        

        if len(searched) > 1 :
            # genres = Genre.objects.all()
            # movie = Movie.objects.get(pk=505642)
            if searched_type == 'all':
                # print(movie.genres.all())
                # genre = Genre.objects.all()
                genre = Genre.objects.filter(name__icontains=searched)
                # print(genre[0].name)
                if genre:
                    movies = Movie.objects.filter(genres__name__icontains=genre[0].name)
                # movie = Movie.objects.get(pk=505642)
                # print(movie)
                    # print(name)
                else:
                    movies = Movie.objects.filter(title__icontains=searched)

            elif searched_type == 'genres':
                genre = Genre.objects.filter(name__icontains=searched)
                if genre:
                    movies = Movie.objects.filter(genres__name__icontains=genre[0].name)

            elif searched_type == 'title':
                movies = Movie.objects.filter(title__icontains=searched)
        
        # else:
        #     return redirect("movies:index")

        context = {
            "movies": movies,
            "searched": searched
        }
        return render(request, "movies/search.html", context)

    return render(request, 'movies/index.html')


# def search(request):
#     searched = request.GET.get("movie")
#     if len(searched) > 1:
#         movie = Movie.objects.filter(title__icontains=searched)
#         context = {
#             "movie": movie
#         }
#     return render(request, "movies/search.html", context)