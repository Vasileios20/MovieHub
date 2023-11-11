from django.shortcuts import render, HttpResponse, redirect
from .models import Favourites, Comment, Movie, Rating
from .movie_details import genre, cast_list, release_date, movie_model
from django.contrib import messages
from .forms import CommentForm
from django.core.paginator import Paginator
from django.http import JsonResponse
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
                  spoken_languages=json.dumps(data["spoken_languages"]),
                  ).save()
    return movie


def rating_average(movie_id):
    """ A view to return the average rating of a movie """
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


def index(request):
    """ A view to return the index page """
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
        width = str(average * 100 / 5) + "%" if average > 0 else "0%"
        temp_average.append(
            {"average": average, "movie_id": movie_obj.movie_id,
             "width": width})
    # Sort the list by the average rating
    temp_average = sorted(
        temp_average, key=lambda d: d['average'], reverse=True)

    # Create list of sorted movies by average rating
    for movie_id in temp_average:
        movie_obj = Movie.objects.get(movie_id=movie_id["movie_id"])
        data = movie_model(movie_obj.movie_id)
        data.update({"movie_obj": movie_obj.movie_id})
        new_list.append(data)
    # Add the list to the movies_list
    movies_list.append(new_list) if len(new_list) > 0 else None

    context = {
        "movies_list": movies_list,
    }
    return render(request, "index.html", context)


def search(request):
    """A view to return the search page"""
    query = request.GET.get("query")
    movies_list = []

    if query:
        # Search the database for the query
        title = Movie.objects.filter(title__icontains=query)
        temp = []
        if title.exists():
            for m in title:
                temp.append({"title": m.title,
                             "movie_id": m.movie_id,
                             "poster_path": m.poster_path,
                             "release_date": m.release_date,
                             })
        # Search the API for the query
        url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={query}"
        response = requests.get(url)
        data = response.json()
        results = data["results"]
        temp_list = []
        # Add the results to a list
        for result in results:
            release_date_new = release_date(request, result["id"])
            temp_list.append(
                {"title": result["title"], "movie_id": result["id"],
                 "poster_path": result["poster_path"],
                 "release_date": release_date_new})
        # Add the results from the database and the API to a list
        temp.extend(temp_list)
        # Remove duplicates from the list
        movie_set = set()
        new_list = []
        for m in temp:
            t = tuple(m.items())
            if t not in movie_set:
                movie_set.add(t)
                new_list.append(m)
        # Add the list to the movies_list
        movies_list.append(new_list) if len(new_list) > 0 else None
    else:
        return HttpResponse("Please enter a search query")

    context = {
        "query": query,
        "movies_list": movies_list,
    }

    return render(request, "search_results.html", context)


def movie_details(request, movie_id):
    """A view to return the movie details page"""
    movie = Movie.objects.filter(movie_id=movie_id)

    if not movie.exists():
        url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}'
        response = requests.get(url)
        data = response.json()
        data.update({"cast": cast_list(request, movie_id),
                     "release_date": release_date(request, movie_id),
                     })

        # Save the movie to the database
        get_movie_detail(request, movie_id)
        movie_obj = Movie.objects.get(movie_id=movie_id)
        data.update({"movie_obj": movie_obj.movie_id})
        return redirect("movie_details", movie_obj)
    else:
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
            # check if the movie is already in the favourites list
            movie_obj = Movie.objects.get(movie_id=movie_id)
            fav_id = Favourites.objects.filter(user=user, movie_id=movie_obj)
            user_rating = Rating.objects.filter(user=user, movie_id=movie_obj)
            if not user_rating.exists():
                rating = "No rating"
            else:
                for r in user_rating:
                    rating = str(r.rating * 20) + "%"
            if fav_id.exists():
                fav = True
            if user_rating.exists():
                rated = True
    average = rating_average(movie_obj.movie_id)
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


def add_favourites(request, movie_id):
    """ A view to add a favourite to a movie """
    user = request.user
    movie_obj = Movie.objects.get(id=movie_id)

    Favourites(user=user, movie_id=movie_obj).save()
    messages.add_message(request, messages.SUCCESS,
                         "Added to favourites")
    return redirect("movie_details", movie_obj)


def remove_favourite(request, movie_id):
    """ A view to remove a favourite from a movie """
    user = request.user
    movie_obj = Movie.objects.filter(movie_id=movie_id)
    for movie in movie_obj:
        Favourites.objects.filter(user=user, movie_id=movie).delete()
    messages.add_message(request, messages.ERROR,
                         "Removed from favourites")
    return redirect("favourites")


def view_favourites(request):
    """ A view to return the favourites page """
    favourites = Favourites.objects.filter(user=request.user)
    fav_movies = favourites.values_list("movie_id", flat=True)
    fav_list = []

    for movie in fav_movies:
        movie_obj = Movie.objects.get(id=movie)
        movie_id = movie_obj.movie_id
        data = movie_model(movie_id)
        data.update({"movie_obj": movie_id})
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
    movie = Movie.objects.filter(id=movie_id).values()
    movie_obj = Movie.objects.get(id=movie_id)
    for m in movie:
        data = movie_model(m['movie_id'])

    comments = Comment.objects.filter(
        movie_id=movie_id).order_by('-created_on')
    paginator = Paginator(comments, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    num_pages = paginator.num_pages
    if num_pages <= 5 or page_obj.number <= 2:
        pages = [x for x in range(1, min(num_pages + 1, 4))]
    elif page_obj.number > num_pages - 1:
        pages = [x for x in range(num_pages - 2, num_pages + 1)]
    else:
        pages = [x for x in range(page_obj.number - 1, page_obj.number + 2)]
    comment_count = Comment.objects.filter(
        movie_id=movie_id, approved=True).count()

    comment_form = CommentForm()
    commented = False

    width = rating_average(movie_obj.movie_id)

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        commented = True

        if comment_form.is_valid():
            comment_form.instance.user = request.user
            comment = comment_form.save(commit=False)
            comment.movie_id = movie_obj
            comment.save()
            messages.success(request, 'Comment added successfully')
            return redirect(
                'comment_movie', movie_id
            )
        else:
            messages.error(request, 'Error adding comment')

    return render(request, "comments.html", {
        "data": data,
        "comment_count": comment_count,
        "comments": comments,
        "commented": commented,
        "page_obj": page_obj,
        "form": comment_form,
        "width": width,
        "pages": pages,
    })


def edit_comment(request, movie_id, comment_id, *args, **kwargs):
    """
    view to edit comments
    """
    if request.method == 'POST':
        user = request.user
        movie_obj = Movie.objects.get(id=movie_id)
        comment = movie_obj.comments.filter(id=comment_id).first()
        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid() and comment.user == user:
            comment = comment_form.save(commit=False)
            comment.movie_id = movie_obj
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return redirect('comment_movie', movie_id)


def delete_comment(request, movie_id, comment_id, *args, **kwargs):
    """
    view to delete comments
    """
    user = request.user
    movie_obj = Movie.objects.get(id=movie_id)
    comment = movie_obj.comments.filter(id=comment_id).first()
    if comment.user == user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment Deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'Error deleting comment!')

    return redirect('comment_movie', movie_id)


def add_rating(request):
    """ A view to add a rating to a movie """
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
