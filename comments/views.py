from django.shortcuts import render, redirect
from .models import Comment
from home.models import Movie
from home.movie_details import movie_model
from django.contrib import messages
from .forms import CommentForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.utils.html import strip_tags
from home.views import rating_average


@login_required
def comment_movie(request, movie_id):
    """ A view to add a comment to a movie.
    This view saves the comment to the database.
    Gets the comments from the database and
    paginates them, gets the number of approved comments
    for the movie and finally gets the average rating and
    calculates the width of the rating bar (stars) for the movie.
    """
    # Get the movie details from the database
    movie = Movie.objects.filter(id=movie_id).values()
    movie_obj = Movie.objects.get(id=movie_id)
    for m in movie:
        data = movie_model(m["movie_id"])

    # Get the comments from the database
    comments = Comment.objects.filter(
        movie_id=movie_id).order_by("-created_on")
    # Paginate the comments
    paginator = Paginator(comments, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    num_pages = paginator.num_pages
    # Create a list of pages to display
    if num_pages <= 5 or page_obj.number <= 2:
        pages = [x for x in range(1, min(num_pages + 1, 4))]
    elif page_obj.number > num_pages - 1:
        pages = [x for x in range(num_pages - 2, num_pages + 1)]
    else:
        pages = [x for x in range(page_obj.number - 1, page_obj.number + 2)]
    # Get the number of comments
    comment_count = Comment.objects.filter(
        movie_id=movie_id, approved=True).count()

    comment_form = CommentForm()
    commented = False

    # Get the average rating for the movie
    average = rating_average(movie_obj.movie_id)
    # Calculate the width of the rating bar (stars)
    width = str(average * 100 / 5) + "%"

    # Check if method is POST and if the form is valid
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        commented = True

        if comment_form.is_valid():
            comment_form.instance.user = request.user
            comment_form.instance.movie_id = movie_obj
            comment = comment_form.cleaned_data['comment']
            comment = strip_tags(comment)
            comment = comment.replace("&nbsp;", " ")
            comment = str(comment).strip()
            comment_form.instance.comment = comment

            # check if the comment is empty
            if comment == '':
                messages.error(request, "You can't submit an empty comment")
            else:
                comment_form.save()
                messages.success(request, "Comment added successfully")
                return redirect(
                    "comment_movie", movie_id
                )
        else:
            messages.error(request, "Error adding comment")

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


@login_required
def edit_comment(request, movie_id, comment_id, *args, **kwargs):
    """ A view to edit the comments."""
    # Check if method is POST and if the form is valid
    if request.method == "POST":
        # Get the comment from the database
        user = request.user
        movie_obj = Movie.objects.get(id=movie_id)
        comment = movie_obj.comments.filter(id=comment_id).first()
        comment_form = CommentForm(data=request.POST, instance=comment)
        # Check if the user is the owner of the comment
        if comment_form.is_valid() and comment.user == user:
            comment_form.instance.movie_id = movie_obj
            comment = comment_form.cleaned_data['comment']
            comment = strip_tags(comment)
            comment = comment.replace("&nbsp;", " ")
            comment = str(comment).strip()
            comment_form.instance.comment = comment
            comment_form.instance.approved = False
            # check if the comment is empty
            if comment == '':
                messages.error(request, "You can't submit an empty comment")
            else:
                comment_form.save()
                messages.add_message(
                    request, messages.SUCCESS, "Comment Updated!")
                return redirect(
                    "comment_movie", movie_id
                )
        else:
            messages.add_message(request, messages.ERROR,
                                 "Error updating comment!")

    return redirect("comment_movie", movie_id)


@login_required
def delete_comment(request, movie_id, comment_id, *args, **kwargs):
    """A view to delete comments."""
    # Get the comment from the database
    user = request.user
    movie_obj = Movie.objects.get(id=movie_id)
    comment = movie_obj.comments.filter(id=comment_id).first()
    # Check if the user is the owner of the comment
    if comment.user == user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, "Comment Deleted!")
    else:
        messages.add_message(request, messages.ERROR,
                             "Error deleting comment!")

    return redirect("comment_movie", movie_id)
