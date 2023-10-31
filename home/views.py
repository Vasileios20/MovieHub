from django.shortcuts import render, HttpResponse, redirect
from .models import Favourites
from .movie_details import genre, cast_list, release_date
from django.contrib import messages
import requests
import os


TMDB_API_KEY = os.environ.get("TMDB_API_KEY")


def index(request):
    """ A view to return the index page """
    movies_list = []

    url = f"https://api.themoviedb.org/3/movie/upcoming?api_key={TMDB_API_KEY}&language=en-US&page=1"
    response = requests.get(url)
    data = response.json()
    results = data["results"]
    temp = []
    for result in results:
        release_date_new = release_date(request, result["id"])
        genres = genre(request, result["id"])
        temp.append(
            {"title": result["title"], "overview": result["overview"],
             "poster_path": result["poster_path"],
             "release_date": release_date_new,
             "genres": genres,
             "movie_id": result["id"]})
    movies_list.append(temp) if len(temp) > 0 else None

    context = {
        "movies_list": movies_list,
    }
    return render(request, "index.html", context)


def search(request):
    """A view to return the search page"""
    query = request.GET.get("query")
    movies_list = []

    if query:
        url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={query}"
        response = requests.get(url)
        data = response.json()
        results = data["results"]

        temp = []
        for result in results:
            release_date_new = release_date(request, result["id"])
            genres = genre(request, result["id"])
            temp.append(
                {"title": result["title"],
                 "poster_path": result["poster_path"],
                 "release_date": release_date_new,
                 "genres": genres,
                 "movie_id": result["id"]})

        movies_list.append(temp) if len(temp) > 0 else None
    else:
        return HttpResponse("Please enter a search query")

    context = {
        "query": query,
        "results_list": movies_list,
    }

    return render(request, "search_results.html", context)


def movie_details(request, movie_id):
    """A view to return the movie details page"""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    response = requests.get(url)
    data = response.json()
    genres = genre(request, movie_id)
    cast = cast_list(request, movie_id)
    release_date_new = release_date(request, data["id"])

    # check if the user is logged in
    user = request.user
    if not user.is_authenticated:
        return render(request, "movie_details.html", {
            "data": data,
            "genres": genres,
            "cast": cast,
            "release_date": release_date_new,
        })
    else:
        # check if the movie is already in the favourites list
        fav_id = Favourites.objects.filter(user=user, movie_id=movie_id)
        fav = bool
        if fav_id.exists():
            fav = True

        context = {
            "data": data,
            "genres": genres,
            "cast": cast,
            "release_date": release_date_new,
            "fav": fav,
        }

        # render the movie details page with the data from the API
        return render(request, "movie_details.html", context)


def add_favourites(request, movie_id):
    """ A view to add a favourite to a movie """
    user = request.user
    fav_id = Favourites.objects.filter(user=user, movie_id=movie_id)

    if fav_id.exists():
        fav_id.delete()
        messages.add_message(request, messages.ERROR,
                             "Removed from favourites")
        return redirect("/favourites/")
    else:
        Favourites(user=user, movie_id=movie_id).save()
        messages.add_message(request, messages.SUCCESS,
                             "Added to favourites")
    return redirect(f"/search_results/{movie_id}/")


def view_favourites(request):
    """ A view to return the favourites page """
    favourites = Favourites.objects.filter(user=request.user)
    fav_movies = favourites.values_list("movie_id", flat=True)
    fav_list = []

    for movie_id in fav_movies:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}"
        response = requests.get(url)
        data = response.json()
        fav_list.append(data)

    if not fav_list:
        return render(request, "favourites.html",
                      {"empty_list": "Your list is empty"
                       }
                      )
    else:
        return render(request,
                      "favourites.html",
                      {"fav_list": fav_list,
                       }
                      )


def comment_movie(request, movie_id):
    """ A view to add a comment to a movie """
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    response = requests.get(url)
    data = response.json()
    genres = genre(request, movie_id)
    cast = cast_list(request, movie_id)
    release_date_new = release_date(request, data["id"])
    
    return render(request, "comments.html", {
        "data": data,
        "genres": genres,
        "release_date": release_date_new,
        "cast": cast,
    })
