from django.shortcuts import render, redirect
from .models import Movie
from ratings.models import Rating
from favourites.models import Favourites
from .movie_details import cast_list, release_date, movie_model
from django.contrib import messages
from ratings.views import rating_average, ratings_list
import json
import requests
import os


TMDB_API_KEY = os.environ.get("TMDB_API_KEY")


def get_movie_detail(request, movie_id):
    """A function to get the movie details from the API
    and save them to the database. It is called from the
    movie_details view if the movie is not in the database.
    param: request : request object
    param: movie_id : movie id
    return: movie object
    """
    # Get the movie details from the API and save them to the database
    url = (
        f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}"
    )
    response = requests.get(url)
    data = response.json()
    movie = Movie(
        movie_id=data["id"],
        title=data["title"],
        overview=data["overview"],
        poster_path=data["poster_path"],
        release_date=release_date(request, movie_id),
        genres=json.dumps(data["genres"]),
        cast=cast_list(request, movie_id),
        revenue=data["revenue"],
        budget=data["budget"],
        runtime=data["runtime"],
        popularity=data["popularity"],
        homepage=data["homepage"],
        production_companies=json.dumps(data["production_companies"]),
        production_countries=json.dumps(data["production_countries"]),
        original_language=data["original_language"],
        original_title=data["original_title"],
        spoken_languages=json.dumps(data["spoken_languages"]),
    ).save()
    return movie


def index(request):
    """A view to return the index page.
    It calls the ratings_list function to get the rated movies list.
    """

    movies_list = ratings_list()

    context = {
        "movies_list": movies_list,
    }
    return render(request, "index.html", context)


def search(request):
    """A view to return the search page.
    Gets the query from the search bar and searches the database
    and the API for the query. If the movie is in the database,
    creates a list , then checks if the movie is in the API results
    and adds it to the list. Then it removes the duplicates from the list.
    """
    # Get the query from the search bar
    query = request.GET.get("query")
    movies_list = []
    query = query.strip()

    # Check if the query is empty
    if query == "":
        messages.error(request, "Please enter a search query")
        return redirect("home")
    else:
        if query:
            # Search the database for the query
            title = Movie.objects.filter(title__icontains=query)
            temp = []
            if title.exists():
                for m in title:
                    temp.append(
                        {
                            "title": m.title,
                            "movie_id": m.movie_id,
                            "poster_path": m.poster_path,
                            "release_date": m.release_date,
                        }
                    )
            # Search the API for the query
            url = (
                f"https://api.themoviedb.org/3/search/movie?"
                f"api_key={TMDB_API_KEY}&query={query}"
            )
            response = requests.get(url)
            data = response.json()
            results = data["results"]
            temp_list = []
            # Add the results to a list
            for result in results:
                release_date_new = release_date(request, result["id"])
                temp_list.append(
                    {
                        "title": result["title"],
                        "movie_id": result["id"],
                        "poster_path": result["poster_path"],
                        "release_date": release_date_new,
                    }
                )
            # Extend the database movie (temp) list with the API temp_list
            temp.extend(temp_list)
            # Remove duplicates from the list
            movie_set = set()
            new_list = []
            for m in temp:
                t = tuple(m.items())
                if t not in movie_set:
                    movie_set.add(t)
                    new_list.append(m)
            # Add the new_list to the movies_list to be displayed
            movies_list.append(new_list) if len(new_list) > 0 else None

    context = {
        "query": query,
        "movies_list": movies_list,
    }

    return render(request, "search_results.html", context)


def movie_details(request, movie_id):
    """A view to return the movie details page.
    It gets the movie details from the database.
    If the movie is not in the database, it calls the
    get_movie_detail function to save the movie details
    and redirects to the rendered movie_details page."""
    movie = Movie.objects.filter(movie_id=movie_id)

    # Check if the movie is in the database
    if not movie.exists():
        url = (
            f"https://api.themoviedb.org/3/movie/{movie_id}?"
            f"api_key={TMDB_API_KEY}"
        )
        response = requests.get(url)
        data = response.json()
        data.update(
            {
                "cast": cast_list(request, movie_id),
                "release_date": release_date(request, movie_id),
            }
        )

        # Save the movie to the database
        get_movie_detail(request, movie_id)
        movie_obj = Movie.objects.get(movie_id=movie_id)
        data.update({"movie_obj": movie_obj.movie_id})
        return redirect("movie_details", movie_obj)
    else:
        # Get the movie details from the database
        data = movie_model(movie_id)
        movie_obj = Movie.objects.get(movie_id=movie_id)
        data.update({"movie_obj": movie_obj.movie_id})

        # check if the user is logged in
        user = request.user
        fav = bool
        rated = bool
        if not user.is_authenticated:
            fav = False
            rated = False
            rating = "You must be logged in to rate this movie"
        else:
            movie_obj = Movie.objects.get(movie_id=movie_id)
            fav_id = Favourites.objects.filter(user=user, movie_id=movie_obj)
            user_rating = Rating.objects.filter(user=user, movie_id=movie_obj)
            # check of the user has rated the movie
            if not user_rating.exists():
                rating = "No rating"
            else:
                for r in user_rating:
                    rating = str(r.rating * 20) + "%"
            # check if the movie is already in the favourites list
            if fav_id.exists():
                fav = True
            # check if the movie is already rated
            if user_rating.exists():
                rated = True
    # Get the average rating for the movie
    average = rating_average(movie_obj.movie_id)
    # Calculate the width of the rating bar (stars)
    width = str(average * 100 / 5) + "%"

    context = {
        "data": data,
        "fav": fav,
        "width": width,
        "rated": rated,
        "rating": rating,
    }
    # render the movie details page with the data from the API
    return render(request, "movie_details.html", context)
