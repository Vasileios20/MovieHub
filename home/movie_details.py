from .models import Movie
import json
import requests
import re
import os


TMDB_API_KEY = os.environ.get("TMDB_API_KEY")


def cast_list(request, movie_id):
    """A view to return the movie cast list"""
    # get the cast list
    url = (
        f"https://api.themoviedb.org/3/movie/{movie_id}/credits?"
        f"api_key={TMDB_API_KEY}&language=en-US"
    )
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
    # get the release date
    url = (f"https://api.themoviedb.org/3/movie/{movie_id}?"
           f"api_key={TMDB_API_KEY}&language=en-US"
           )
    response = requests.get(url)
    data = response.json()
    # format the release date
    release_date_before = data["release_date"]
    release_date_new = re.findall(r"\d+", release_date_before)[::-1]
    release_date = "/".join([str(elem) for elem in release_date_new])
    return release_date


def movie_model(movie_id):
    """A view to return the movie model"""
    # get the movie model
    movie = Movie.objects.filter(movie_id=movie_id).values()
    data = {}
    # get the movie details
    for mov in movie:
        jsonDec = json.decoder.JSONDecoder()
        genres = jsonDec.decode(mov["genres"])
        production_companies = jsonDec.decode(mov["production_companies"])
        production_countries = jsonDec.decode(mov["production_countries"])
        spoken_languages = jsonDec.decode(mov["spoken_languages"])
        data.update({"title": mov["title"],
                     "poster_path": mov["poster_path"],
                     "overview": mov["overview"],
                     "release_date": mov["release_date"],
                     "revenue": mov["revenue"],
                     "budget": mov["budget"],
                     "runtime": mov["runtime"],
                     "popularity": mov["popularity"],
                     "homepage": mov["homepage"],
                     "production_companies": production_companies,
                     "production_countries": production_countries,
                     "spoken_languages": spoken_languages,
                     "original_language": mov["original_language"],
                     "original_title": mov["original_title"],
                     "cast": mov["cast"],
                     "genres": genres,
                     "movie_id": mov["id"]})
    return data
