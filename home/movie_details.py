import requests
import re
import os


TMDB_API_KEY = os.environ.get("TMDB_API_KEY")


def genre(request, movie_id):
    """A view to return the movie genres"""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    response = requests.get(url)
    data = response.json()
    genres_list = []
    for genre in data["genres"]:
        genres_list.append(genre["name"])
    genres = ", ".join([str(elem) for elem in genres_list])
    return genres


def cast_list(request, movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={TMDB_API_KEY}&language=en-US"
    response = requests.get(url)
    data = response.json()
    # sort the cast by popularity
    temp_cast_list = []
    for cast in data["cast"]:
        temp_cast_list.append(
            {"name": cast["name"], "popularity": cast["popularity"]})
    sorted_cast_list = sorted(temp_cast_list, key=lambda d: d["popularity"],
                              reverse=True)
    cast_list = []
    for name in sorted_cast_list:
        cast_list.append(name["name"])

    cast = ", ".join([str(elem) for elem in cast_list])
    return cast


def release_date(request, movie_id):
    """A view to return the movie release date"""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    response = requests.get(url)
    data = response.json()
    release_date_before = data["release_date"]
    release_date_new = re.findall(r"\d+", release_date_before)[::-1]
    release_date = "/".join([str(elem) for elem in release_date_new])
    return release_date
