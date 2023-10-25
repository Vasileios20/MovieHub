from django.shortcuts import render, HttpResponse
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
