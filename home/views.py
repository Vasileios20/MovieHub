from django.shortcuts import render, HttpResponse, redirect
from .models import Favourites, Comment, Movie
from .movie_details import genre, cast_list, release_date
from django.contrib import messages
from .forms import CommentForm
from django.core.paginator import Paginator
import json
import requests
import os


TMDB_API_KEY = os.environ.get("TMDB_API_KEY")


def get_movie_detail(request, movie_id):
    """ A view to return the movie details """
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}'
    response = requests.get(url)
    data = response.json()
    movie = Movie(movie_id=data["id"], title=data["title"],
                  overview=data["overview"], poster_path=data["poster_path"],
                  release_date=release_date(request, movie_id),
                  genres=json.dumps(data["genres"]),
                  cast=cast_list(request, movie_id), revenue=data["revenue"],
                  budget=data["budget"], runtime=data["runtime"],
                  popularity=data["popularity"], homepage=data["homepage"],
                  production_companies=json.dumps(
                      data["production_companies"]),
                  production_countries=json.dumps(
                      data["production_countries"]),
                  original_language=data["original_language"],
                  original_title=data["original_title"],
                  spoken_languages=json.dumps(data["spoken_languages"]),).save()
    return movie


def movie_model(movie_id):
    movie = Movie.objects.all().values()
    data = {}
    for mov in movie:
        if mov["movie_id"] == movie_id:
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
                         "vote_average": mov["vote_average"],
                         "vote_count": mov["vote_count"],
                         "cast": mov["cast"],
                         "genres": genres,
                         "movie_id": mov["id"]})
    return data


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
    movie = Movie.objects.filter(movie_id=movie_id)

    if movie.exists():
        data = movie_model(movie_id)
        return render(request, "movie_details.html", {
            "data": data,
        })
    else:
        url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}'
        response = requests.get(url)
        data = response.json()
        data.update({"cast": cast_list(request, movie_id),
                     "release_date": release_date(request, movie_id),
                     })

        # Save the movie to the database
        get_movie_detail(request, movie_id)
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

    comments = Comment.objects.filter(movie_id=movie_id, approved=True)
    paginator = Paginator(comments, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    comment_count = Comment.objects.filter(
        movie_id=movie_id, approved=True).count()

    comment_form = CommentForm(data=request.POST)

    if request.method == 'POST':

        if comment_form.is_valid():
            comment_form.instance.user = request.user
            comment = comment_form.save(commit=False)
            comment.movie_id = movie_id
            comment.save()
            messages.success(request, 'Comment added successfully')
        else:
            comment_form = CommentForm()

        return render(request, "comments.html", {
            "data": data,
            "genres": genres,
            "release_date": release_date_new,
            "cast": cast,
            "comment_count": comment_count,
            "comments": comments,
            "commented": True,
            "page_obj": page_obj,
            "form": CommentForm(),
        })
    else:
        return render(request, "comments.html", {
            "data": data,
            "genres": genres,
            "release_date": release_date_new,
            "cast": cast,
            "comment_count": comment_count,
            "comments": comments,
            "commented": False,
            "page_obj": page_obj,
            "form": CommentForm(),
        })
