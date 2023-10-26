from django.shortcuts import render, HttpResponse, redirect
from .models import Favourites
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
        temp.append(
            {"title": result["title"], "overview": result["overview"],
             "poster_path": result["poster_path"],
             "release_date": result["release_date"],
             "movie_id": result["id"]})
    movies_list.append(temp) if len(temp) > 0 else None
    genres = genre(request, results, result["id"])

    context = {
        "movies_list": movies_list,
        "genres": genres,
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
            temp.append(
                {"title": result["title"],
                 "poster_path": result["poster_path"],
                 "release_date": result["release_date"],
                 "movie_id": result["id"]})

        movies_list.append(temp) if len(temp) > 0 else None
    else:
        return HttpResponse("Please enter a search query")

    context = {
        "query": query,
        "results_list": movies_list,
    }

    return render(request, "search_results.html", context)


def genre(request, data, movie_id):
    """A view to return the movie genres"""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    response = requests.get(url)
    data = response.json()
    genres_list = []
    for genre in data["genres"]:
        genres_list.append(genre["name"])
    genres = ", ".join([str(elem) for elem in genres_list])
    return genres


def cast_list(request, data, movie_id):
    url_cast = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={TMDB_API_KEY}&language=en-US"
    response_cast = requests.get(url_cast)
    data_cast = response_cast.json()
    # sort the cast by popularity
    temp_cast_list = []
    for cast in data_cast["cast"]:
        temp_cast_list.append(
            {"name": cast["name"], "popularity": cast["popularity"]})
    sorted_cast_list = sorted(temp_cast_list, key=lambda d: d["popularity"],
                              reverse=True)
    cast_list = []
    for name in sorted_cast_list:
        cast_list.append(name["name"])

    cast = ", ".join([str(elem) for elem in cast_list])
    return cast


def movie_details(request, movie_id):
    """A view to return the movie details page"""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    response = requests.get(url)
    data = response.json()
    genres = genre(request, data, movie_id)
    cast = cast_list(request, data, movie_id)

    context = {
        "data": data,
        "genres": genres,
        "cast": cast,
    }

    # render the movie details page with the data from the API
    return render(request, "movie_details.html", context)


def add_favourites(request, movie_id):
    """ A view to add a favourite to a movie """
    user = request.user
    fav_id = Favourites.objects.filter(user=user, movie_id=movie_id)

    if fav_id.exists():
        fav_id.delete()
        return redirect("/favourites/")
    else:
        Favourites(user=user, movie_id=movie_id).save()

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
        genres = genre(request, data, movie_id)

    if not fav_list:
        return render(request, "favourites.html",
                      {"empty_list": "Your list is empty"
                       }
                      )
    else:
        return render(request,
                      "favourites.html",
                      {"fav_list": fav_list,
                       "genres": genres,
                       }
                      )
