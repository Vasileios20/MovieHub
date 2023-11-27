from django.shortcuts import render, redirect
from .models import Favourites
from home.models import Movie
from home.movie_details import movie_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def add_favourites(request, movie_id):
    """ A view to add a favourite to a movie.
    Gets the movie details from the database and
    saves them to the favourites table.
    """
    user = request.user
    movie_obj = Movie.objects.get(id=movie_id)

    Favourites(user=user, movie_id=movie_obj).save()
    messages.add_message(request, messages.SUCCESS,
                         "Added to favourites")
    return redirect("movie_details", movie_obj)


@login_required
def remove_favourite(request, movie_id):
    """ A view to remove a favourite from a movie.
    Gets the movie details from the database and
    removes them from the favourites table.
    """
    user = request.user
    movie_obj = Movie.objects.filter(movie_id=movie_id)
    for movie in movie_obj:
        Favourites.objects.filter(user=user, movie_id=movie).delete()
    messages.add_message(request, messages.ERROR,
                         "Removed from favourites")
    return redirect("favourites")


@login_required
def view_favourites(request):
    """ A view to return the favourites page.
    Gets the user's favourites list from the database
    and renders the favourites page with the list.
    If the list is empty, it renders the favourites page
    with a message.
    """
    # Get the favourites from the database
    favourites = Favourites.objects.filter(user=request.user)
    fav_movies = favourites.values_list("movie_id", flat=True)
    fav_list = []

    # Get the movie details from the database update the details
    # with the movie id and add them to a list
    for movie in fav_movies:
        movie_obj = Movie.objects.get(id=movie)
        movie_id = movie_obj.movie_id
        data = movie_model(movie_id)
        data.update({"movie_obj": movie_id})
        fav_list.append(data)

    # Check if the list is empty
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
