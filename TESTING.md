# Contents

* [HTML](#html)
* [CSS](#css)
* [JSHint](#jshint)
* [CI python linter](#ci-python-linter)
* [Lighthouse](#lighthouse)
* [User Stories](#user-stories)
* [Manual Testing](#manual-testing)
* [Bugs](#bugs)

## HTML

[HTML Validator](https://validator.w3.org/)

[Home](documentation/testing/html-vld/index-html-vld.png)

[About](documentation/testing/html-vld/about-html-vld.png)

[Contact](documentation/testing/html-vld/contact-html-vld.png)

[Ratings](documentation/testing/html-vld/ratings-html-vld.png)

[Login](documentation/testing/html-vld/login-html-vld.png)

[Logout](documentation/testing/html-vld/logout-html-vld.png)

[Sign up]()

[Movie](documentation/testing/html-vld/movie-html-vld.png)

[Favourites](documentation/testing/html-vld/favourites-html-vld.png)

[Comments](documentation/testing/html-vld/comments-html-vld.png)

[Results](documentation/testing/html-vld/results-html-vld.png)

## CSS

[CSS Jigsaw](https://jigsaw.w3.org/css-validator/)

[CSS](documentation/testing/css-vld/css-vld.png)

## JSHint

[JShint](https://jshint.com/)

[script.js](/documentation/testing/jshint/script-jsh.png)

[comments.js](/documentation/testing/jshint/comments-jsh.png)

[rating.js](/documentation/testing/jshint/rating-jsh.png)

## CI Python linter

[pep8ci](https://pep8ci.herokuapp.com/)

|App/File|views.py|urls.py|models.py|admin.py|forms.py|movie_details.py|
|--|--|--|--|--|--|--|
|movieHub|[PASS](documentation/testing/pep8/mh-views.png)|[PASS](documentation/testing/pep8/mh-urls.png)|n/a|n/a|n/a|n/a|
|home|[PASS](documentation/testing/pep8/home-views.png)|[PASS](documentation/testing/pep8/home-urls.png)|[PASS](documentation/testing/pep8/home-models.png)|[PASS](documentation/testing/pep8/home-admin.png)|[PASS](documentation/testing/pep8/home-forms.png)|[PASS](documentation/testing/pep8/home-movie-details.png)|
|about|[PASS](documentation/testing/pep8/about-views.png)|[PASS](documentation/testing/pep8/about-urls.png)|n/a|n/a|n/a|n/a|
|contact|[PASS](documentation/testing/pep8/contact-views.png)|[PASS](documentation/testing/pep8/contact-urls.png)|[PASS](documentation/testing/pep8/contact-models.png)|[PASS](documentation/testing/pep8/contact-admin.png)|[PASS](documentation/testing/pep8/contact-forms.png)|n/a|

## Lighthouse

[Home](documentation/testing/lighthouse/index-lh.png)

[About](documentation/testing/lighthouse/about-lh.png)

[Contact](documentation/testing/lighthouse/contact-lh.png)

[Ratings](documentation/testing/lighthouse/ratings-lh.png)

[Login](documentation/testing/lighthouse/login-lh.png)

[Logout](documentation/testing/lighthouse/logout-lh.png)

[Sign up](documentation/testing/lighthouse/signup-lh.png)

[Movie](documentation/testing/lighthouse/movie-lh.png)

[Favourites](documentation/testing/lighthouse/favourites-lh.png)

[Comments](documentation/testing/lighthouse/comments-lh.png)

[Results](documentation/testing/lighthouse/results-lh.png)

## User Stories

|User story|How was achieved|PASS|
|--|--|--|
|As a Site Admin I can approve comments so that I can filter out objectionable comments|[Approve comment](/documentation/features/admin-appr.png) functionality has been implenented for at admin site| :heavy_check_mark: |
|As a Site User I can register an account so that I can comment and give rating to a movie and create favourites list| User can register an account through the [sign up](/documentation/features/signup.png) proccess implemented| :heavy_check_mark: |
|As a Site User I can search for a movie so that I can select one|The user can search a movie in the search bar inluded in the [navbar](/documentation/features/navbar.png) accross all pages| :heavy_check_mark: |
|As a Site User I can view movie details so that I can find more details about the movie|[View details](/documentation/features/results.png) button has been added to the list of movies have been searched| :heavy_check_mark: |
|As a Site User I can write a message to a contact form so that I can communicate with the admin|A [contact page](/documentation/features/contact.png) with a form has been added, where a user can send a message to the admin| :heavy_check_mark: |
|As a Site User I can visit an about page so that I can find more information about the site|[About page](/documentation/features/about.png) with info about the website has been added| :heavy_check_mark: |
|As a Site User I can visit a page so that I can view the top rated movies|[Top 15 Movies page](/documentation/features/ratings.png) with info about the website has been added| :heavy_check_mark: |
|As a Registered User I can view comments on a movie so that I can read the conversation|A [comment page](/documentation/features/comments.png) has been implemented for each [movie](/documentation/features/movie.png)| :heavy_check_mark: |
|As a Registered User I can access a webpage where I can comment on a movie so that I can be involved in the conversation|A [comment page](/documentation/features/comments.png) has been implemented for each movie where there is a [comment section](/documentation/features/comments-ckeditor.png) with a text editor to leave a comment| :heavy_check_mark: |
|As a Registered User I can click to add a movie to my favourites list so that I can have my favourites movies organised|[Add to favourites](/documentation/features/favourites-add.png) functionality has been implemented when the user view the movie details page| :heavy_check_mark: |
|As a Registered User I can click to remove a movie from my favourites so that I can update my favourites list|[Remove from favourites](/documentation/features/favourites-delete.png) functionality has been implemented when the user view the [favourites](/documentation/features/favourites.png) page| :heavy_check_mark: |
|As a Registered User I can add rating to a movie so that I can express how much I liked a movie|[Star rating](/documentation/features/add-rating.png) functionality has been implemented when the user view the movie details page| :heavy_check_mark: |
|As a Registered User I can delete comments from a movie so that manage the content on the platform more effectively|[Delete](/documentation/features/comments-delete.png) comment button has been added to the comment section. When Clicked the [modal](/documentation/features/comments-delete-modal.png) pops up with a delete confirmation message| :heavy_check_mark: |
|As a Registered User I can edit my comments so that manage the content on the platform more effectively|[Edit](/documentation/features/comments-update.png) comment button has been added to the comment section. When Clicked scrolls page to the text editor and change the value of the button submit to update| :heavy_check_mark: |

## Manual Testing

|Feature|Expected Outcome|Testing Performed|Result|Pass|
|--|--|--|--|--|
|Navbar (All Users)|
|Logo button|Redirect to home page|Clicked button|Redirected to home page| :heavy_check_mark: |
|Home button|Redirect to home page|Clicked button|Redirected to home page| :heavy_check_mark: |
|About button|Redirect to about page|Clicked button|Redirected to about page| :heavy_check_mark: |
|Contact us button|Redirect to contact page|Clicked button|Redirected to contact page| :heavy_check_mark: |
|Top 15 Movies button|Redirect to ratings page|Clicked button|Redirected to ratings page| :heavy_check_mark: |
|Search form|Redirect to results page of query entered|Entered a query and clicked search button|Redirected to results page and query results displayed| :heavy_check_mark: |
||If empty return redirect or http response??|
|Navbar(Site User)|
|Sign up us button|Redirect to signup page|Clicked button|Redirected to signup page| :heavy_check_mark: |
|Login button|Redirect to login page|Clicked button|Redirected to login page| :heavy_check_mark: |
|Navbar (Registered User)|
|Logout button|Redirect to logout page|Clicked button|Redirected to logout page| :heavy_check_mark: |
|Favourites button|Redirect to favourites page|Clicked button|Redirected to favourites page| :heavy_check_mark: |
||
|Login Page|
|Login form success|Login user, redirect to home page and display a success message that the user has logged in|Entered username and password, clicked login button|Logged in and redirected to home page, [success message](/documentation/testing/features/login-message.png) displayed| :heavy_check_mark: |
|Login form error|Return error if username or password is wrong|Entered wrong username and password, clicked login button|Error message displayed| :heavy_check_mark: |
|Reset password button|Redirect to reset password page|Clicked reset password button|Redirected to reset password page| :heavy_check_mark: |
||
|Reset password page|
|Reset my password form|Redirect to reset password page with a message that email sent|Entered email address and clicked reset password button|Email recieved and [redirected](/documentation/testing/features/password-reset-sent.png) to reset password page with a confirmation message| :heavy_check_mark: |
||
|Logout Page|
|Logout button|Logout user, redirect to home page and display a success message that the user was logged out|Clicked button|Redirected to home page, [success message](/documentation/testing/features/logout-message.png) displayed| :heavy_check_mark: |
||
|Sign up Page|
|Sign up form success|Register user, redirect to confirm-email page, display a success message that an email had been sent|Entered email address, username and password, clicked sign up button|Redirected to home page, success message dispalyed, verification email received| :heavy_check_mark: |
|Sign up form error|Return error if username exists|Entered a username already in use, clicked sign up button|Error message displayed| :heavy_check_mark: |
||Return error if password doesn't match|Entered 2 different passwords, clicked sign up button|Error message displayed| :heavy_check_mark: |
||Return error if email exists|Entered email already in use, clicked sign up button|Received email stating that "an account using that email address already exists"| :heavy_check_mark: |
||
|Home Page|
||Display top 3 rated movies|Navigated to home page|Top 3 movies were displayed| :heavy_check_mark: |
|View details button|Redirect to movie page and display movie details|Clicked view details button|Redirected to movie page and movie details were displayed| :heavy_check_mark: |
||
|Contact Page|
|Contact form success|Submit form, display success message, send email to admin email address, save the form to the database|Completed the form and clicked submit button|Form was submitted, success message displayed, email with the form details received, form was saved in the database| :heavy_check_mark: |
|Contact form error|Display error message for each field with a wrong input|Left all the fields blank and clicked submit button|Error message for each field was displayed| :heavy_check_mark: |
|||Added whitespaces to each field and clicked submit button|Error message for each field was displayed| :heavy_check_mark: |
|||The above test was repeated with one field blank at a time|Error message for each field was displayed| :heavy_check_mark: |
|||At email address field entered wrong format of email and clicked submit button|Error message to insert the correct email address format was displayed| :heavy_check_mark: |
||
|Top 15 Movies Page|
||Display the top 15 movies|Navigated to the Top 15 Movies(ratings) Page|Top 15 movies were displayed| :heavy_check_mark: |
|Get rated movies in descending|In views.py entered a print statement|Navigated to Top 15 Movies(ratings) Page|All rated movies printed in descending order| :heavy_check_mark: |
|View details button|Redirect to movie page and display movie details|Clicked view details button|Redirected to movie page and movie details were displayed| :heavy_check_mark: |
||
|Favourites Page(Registered User)|
||Display user's favourite movies list|Navigated to the Favourites Page|User's favourite movies were displayed| :heavy_check_mark: |
|Get favourite movies for logged in user|In views.py entered a print statement|Navigated to Favourites Page|User's favourite movies list printed| :heavy_check_mark: |
|View details button|Redirect to movie page and display movie details|Clicked view details button|Redirected to movie page and movie details were displayed| :heavy_check_mark: |
|Remove from favourites button|Remove a movie from the favourites list, display a success message|Clicked remove from favourites button|The movie was removed from favourites list, [success message](/documentation/testing/features/favourites-deleted.png) displayed| :heavy_check_mark: |
||
|Movie Page|
|(All users)|Display movie details|Navigated to the movie page|All movie details retreived from database and displayed| :heavy_check_mark: |
|(Site User)|Not displaying the add favourites button and the add your rating stars|Navigated to the movie page as an unregistered user|The add favourites button and the add your rating stars were not displayed| :heavy_check_mark: |
|Add favourites button(Registered user)|Add a movie to the favourites list, redirect to the movie page display the favourites button checked (disabled) and a success message|Clicked add favourites button|The movie was added to the favourites list, redirected to the movie page and displayed the favourites button checked (disabled) and the [success message](/documentation/testing/features/favourites-added.png)| :heavy_check_mark: |
|Add rating(Registered user)|Send rating data to database, redirect to movie with updated the rating average(stars), display user's rating(stars) and a success message|Clicked add favourites button|The movie was added to the favourites list, redirected to the movie page and displayed the favourites button checked (disabled) and the [success message](/documentation/testing/features/rating-added.png)|Clicked on a star|Rating was saved in database, redirected to movie page, rating average updated, user's rating displayed| :heavy_check_mark: |
|Comments button(Site user)|Redirect to login page|Clicked comments button|Redirected to login page| :heavy_check_mark: |
|Comments button(Registered user)|Redirect to comment page|Clicked comments button|Redirected to comment page| :heavy_check_mark: |
|Movie's homepage button|Open in a new browser tab the movie's homepage link|Clicked movie's homepage button|Opened a new broweser tab with the movie's homepage| :heavy_check_mark: |
||
|Results Page(All users)|
||Display results page of query entered|Entered a query to the search form in navbar and clicked search button|Redirected to results page and query results displayed| :heavy_check_mark: |
|View details button|Redirect to movie page and display movie details, save the movie in the database|Clicked view details button|Redirected to movie page and movie details were displayed, movie saved in the database| :heavy_check_mark: |
||Display movies both from the database and the [TMDB API](https://www.themoviedb.org/)|In the views.py entered one print statement for the database movies and one for movies retreived from the TMDB API, entered a query, that is already in the database, to the search form and clicked search|In the terminal [printed](/documentation/testing/features/results-print.png) movies both from the database and the TMDB API | :heavy_check_mark: |
||
|Comment Page(Registered User)|
|Comment count|Display number of approved comments|Entered and approved 4 comments|Comment counting displayed 4| :heavy_check_mark: |
|Click on textarea to enter a comment|Hide the textarea and display ckeditor|Clicked on textarea|Textearea was hidden and ckeditor displayed| :heavy_check_mark: |
|Comment form success|Display a message "awaiting for approval", display comment faded, display delete and edit buttons, display a success message|Entered a test comment|Displayed awaiting approval message, faded comment, delete and edit buttons, and [success message](/documentation/testing/features/comment-added.png)| :heavy_check_mark: |
|Comment form error|Display error message|Left the comment form blank|Error message was displayed| :heavy_check_mark: |
|Comment form error|Display error message|Entered only whitespaces|Error message was displayed| :heavy_check_mark: |
|Display Delete and Edit buttons only of the user's own comments|Entered and aproved comments with diffirent accounts|Delete and Edit buttons displayed only for logged in user own comments| :heavy_check_mark: |
|Delete button|Display delete modal to confirm deletion|Clicked delete button|Delete modal was displayed| :heavy_check_mark: |
|Delete Modal|
|Delete button|Delete comment and display success message|Clicked delete button|Comment was deleted and [success message](/documentation/testing/features/comments-deleted.png) displayed| :heavy_check_mark: |
|Edit button|Scroll to ckeditor and change submit's button value to "Update"|Clicked edit button|Screen scrolled to ckeditor, submit button's value changed to ["Update"](/documentation/testing/features/comments-update.png)| :heavy_check_mark: |
|Update comment form success|Display a message "awaiting for approval", display comment faded, display delete and edit buttons, and a success message|Clicked on edit button and entered a test comment|Displayed awaiting approval message, faded comment, delete and edit buttons, and the success message| :heavy_check_mark: |
|Comment pagination|Display up to 10 comments|Entered and approved more than 10 comments|10 comments displayed on each page| :heavy_check_mark: |
||If more than 10 comments, display pagination with highlighted active page number(page of comments user is viewing), the total amount of pages, a range of three pages(one before/active/one after), previous and next buttons|Entered and approved more than 10 comments|Highlighted active page number, total amount of pages, a range of three pages, previous and next buttons were displayed| :heavy_check_mark: |
|Pagination next button|Redirect to the next page of comments|Clicked next button|Redirected to the next page of comments| :heavy_check_mark: |
|Pagination previous button|Redirect to the previous page of comments|Clicked previous button|Redirected to the previous page of comments| :heavy_check_mark: |
|Pagination click on a page number|Redirect to the clicked page|Clicked on a number|Redirected to the page clicked| :heavy_check_mark: |
||
|Footer|
|GitHub link|Open the link in a new browser tab|Clicked GitHub link|Opened the link in a new browser tab| :heavy_check_mark: |
|LinkedIn link|Open the link in a new browser tab|Clicked LinkedIn link|Opened the link in a new browser tab| :heavy_check_mark: |
|TMDB link|Open the link in a new browser tab|Clicked TMDB link|Opened the link in a new browser tab| :heavy_check_mark: |
|Contact us button|Redirect to contact page|Clicked Contact Us button|Redirected to contact page| :heavy_check_mark: |
||
|Scroll to top button|Scroll to top of the screen|Clicked button| :heavy_check_mark: |

## Bugs

### Solved Bugs

|#|Bug|Fix|
|--|--|--|
|1|Admin site won't show properly in deployed site.|Installed Whitenoise|
|2|Displaying all the movies in the favourites list from all users|Filter object by user|

||||
|--|--|--|
|3|Movies were stored and in the Comment model by title instead of movie_id|Update def in Movie model to return

```python
Class Movie(models.Model):
...
    def __str__(self):
            return f"{self.movie_id}"
```

||||
|--|--|--|
|4|I couldn't retrieve the data from Movie model to function movie_model()|Instead of getting Movie.objects.all() changed it to Movie.objects.filter(movie_id=movie_id).values() and remove if statement inside the for loop|

```python
def movie_model(movie_id):
    movie = Movie.objects.filter(movie_id=movie_id).values()
    ...
```

||||
|--|--|--|
|5|When I created the Movie model to save the movies that a user would first visit it wouldn't load the page. There was an error with the url for comments and favourites buttons, as both was setup to save in the database with the ID from a Movie object|In the function movie_details once I saved the first time visited movie in my database, I  updated the data dictionarywith the movie_id from the Movie model.|

```python
def movie_details(request, movie_id):
    ...
    data = movie_model(movie_id)
    movie_obj = Movie.objects.get(movie_id=movie_id)
    data.update({"movie_obj": movie_obj.movie_id})
    ...
```
