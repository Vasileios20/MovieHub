from django.shortcuts import render
from .models import Rating
from home.models import Movie
from home.movie_details import movie_model
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


def rating_average(movie_id):
    """ A function to return the average rating of a movie.
    Gets the movie object from the database and the ratings for the movie.
    Creates a list of the ratings and calculate the average.
    If there are no ratings, return 0.
    param: movie_id : movie id
    return: average rating
    """
    movie_obj = Movie.objects.get(movie_id=movie_id)

    ratings = Rating.objects.filter(movie_id=movie_obj)
    rating_list = []
    for rating in ratings:
        rating_list.append(rating.rating)
    if len(rating_list) > 0:
        average = round(sum(rating_list) / len(rating_list), 1)
    else:
        average = 0
    return average


def ratings_list():
    """ A function to return the rated movies list.
    It is called from the index and ratings views.
    return: movies_list (a list of rated movies in descending order)
    """
    movies_list = []
    temp = []
    temp_average = []
    new_list = []

    movies_rating = Rating.objects.all().values_list("movie_id", flat=True)
    for movie in movies_rating:
        temp.append(movie)
    # Create a list of unique movie ids to avoid duplicates
    temp = list(dict.fromkeys(temp))

    # Create a list of movies with the average rating
    for movie_id in temp:
        movie_obj = Movie.objects.get(id=movie_id)
        average = rating_average(movie_obj.movie_id)
        temp_average.append(
            {"average": average, "movie_id": movie_obj.movie_id})
    # Sort the list by the average rating
    temp_average = sorted(
        temp_average, key=lambda d: d["average"], reverse=True)

    # Create list of sorted movies by average rating
    for movie_id in temp_average:
        movie_obj = Movie.objects.get(movie_id=movie_id["movie_id"])
        average = rating_average(movie_obj.movie_id)
        width = str(average * 100 / 5) + "%" if average > 0 else "0%"
        data = movie_model(movie_obj.movie_id)
        data.update({"movie_obj": movie_obj.movie_id,
                     "width": width})
        new_list.append(data)
    # Add the new_list to the movies_list to be displayed
    movies_list.append(new_list) if len(new_list) > 0 else None
    return movies_list


def view_ratings(request):
    """ A view to return the ratings page.
     It calls the ratings_list function to get the rated movies list.
    """

    movies_list = ratings_list()

    context = {
        "movies_list": movies_list,
    }
    return render(request, "ratings.html", context)


@login_required
def add_rating(request):
    """ A view to add a rating to a movie."""
    # Check if method is POST and if the rating exists
    if request.method == "POST":
        user = request.user
        movie_id = request.POST.get("movie_id")
        rating = request.POST.get("rating")
        movie_obj = Movie.objects.get(id=movie_id)
        rate = Rating.objects.filter(user=user, movie_id=movie_obj)
        if not rate.exists():
            Rating(user=user, movie_id=movie_obj, rating=rating).save()
            messages.add_message(request, messages.SUCCESS,
                                 "Rating added successfully")

    return JsonResponse({"success": True}, status=200)
