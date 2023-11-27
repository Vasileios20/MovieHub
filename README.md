# VastMovieHub

![Home Page](documentation/features/index.png)

The VastMovieHub has been developed for my PP4 for Code Institute. At the VastMovieHub the user can search for a movie, see top 15 movies and view a movie's details.
A registered user can also add/delete movies to their favourites list, comment on a movie and edit/delete their comment and give rating to a movie.

This website uses [TMDB](https://www.themoviedb.org/) and the TMDB APIs but is not endorsed, certified, or otherwise approved by TMDB.

![GitHub contributors](https://img.shields.io/badge/CONTRIBUTORS-1-<RED>) ![W3C validation](https://img.shields.io/badge/W3C-VALIDATED-<GREEN>)

[View the deployed project here](https://moviehub-vas-2ed6679610a9.herokuapp.com/)

## Contents

* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Wireframes](#wireframes)
* [User Experience (UX)](#user-experience-ux)
  * [Agile methodology](#agile-methodology)
  * [User Stories](#user-stories)
* [Database Diagram](#database-diagram)
* [Features](#features)
  * [Navigation Bar](#navigation-bar)
  * [Home Page](#home-page)
  * [About Page](#about-page)
  * [Contact Page](#contact-page)
  * [Top 15 Movies Page](#top-15-movies-page)
  * [Login Page](#login-page)
  * [Logout Page](#logout-page)
  * [Signup Page](#signup-page)
  * [Favourites Page](#favourites-page)
    * [Remove Favourite Modal](#remove-favourite-modal)
  * [Search Results Page](#search-results-page)
  * [Movie Details Page](#movie-details-page)
  * [Comments Page](#favourites-page)
    * [Delete Comment Modal](#delete-comment-modal)
  * [403 error Page](#403-error-page)
  * [404 error Page](#404-error-page)
  * [405 error Page](#405-error-page)
  * [500 error Page](#500-error-page)
* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)
* [Deployment and Local Development](#deployment-and-local-development)
  * [Local Development](#local-development)
    * [How to fork](#how-to-fork)
    * [How to clone](#how-to-clone)
    * [Deployment](#deployment)
* [Testing](#testing)
* [Credits](#credits)

## Design

This project uses the Bootstrap Framework and I chose
to use the colours and fonts that it offers.

### Colour Scheme

   [buttons](/documentation/colors/btn-colors.png)

   [navbar](/documentation/colors/bg-dark.png)

### Typography

   Bootstrap's Native font stack

   [Read more about Native font stack](https://www.smashingmagazine.com/2015/11/using-system-ui-fonts-practical-guide/)

### Wireframes

#### Desktop

[Home Page Site user](/documentation/wireframes_diagrams/home_page.png)

[Navbar Registered User](/documentation/wireframes_diagrams/navbar_registered.png)

[About Page](/documentation/wireframes_diagrams/about.png)

[Contact page](/documentation/wireframes_diagrams/contact.png)

[Top 15 Movies](/documentation/wireframes_diagrams/top_rated.png)

[Login](/documentation/wireframes_diagrams/login.png)

[Signup](/documentation/wireframes_diagrams/signup.png)

[Results Page](/documentation/wireframes_diagrams/movie_list.png)

[Movie Page](/documentation/wireframes_diagrams/movie_details.png)

[Favourites Page](/documentation/wireframes_diagrams/favourites_page.png)

[Comments Page](/documentation/wireframes_diagrams/comment_page.png)

#### Mobile

[Home Page](/documentation/wireframes_diagrams/mobile_home.png)

[About Page](/documentation/wireframes_diagrams/mobile_about.png)

[Contact page](/documentation/wireframes_diagrams/mobile_contact.png)

[Top 15 Movies](/documentation/wireframes_diagrams/mobile_top_rated.png)

[Login](/documentation/wireframes_diagrams/mobile_login.png)

[Signup](/documentation/wireframes_diagrams/mobile_signup.png)

[Results Page](/documentation/wireframes_diagrams/mobile_movie_list.png)

[Movie Page](/documentation/wireframes_diagrams/mobile_movie_details.png)

[Favourites Page](/documentation/wireframes_diagrams/mobile_favourites.png)

[Comments Page](/documentation/wireframes_diagrams/mobile_comments.png)

## User Experience (UX)

## Agile Methodology

The Agile Methodology was used to plan this project. This was implemented through Github and the Project Board. Through the use of the Kanban board in the projects view in Github, the project was divided into a few different sections:

* To Do - (All the User stories were initially entered in the 'To Do' column)
* In Progress - (then during development story they were moved into the 'In Progress' column)
* Done - (then finally they get moved into 'Done' once the development completes)
* Future features - (User stories to be implemented in the future)

Please find my Kanban Board with my user stories [here](https://github.com/users/Vasileios20/projects/5).

### User Stories

* As a Site Admin I can approve comments so that I can filter out objectionable comments.
* As a Site User I can register an account so that I can comment and give rating to a movie and create favourites list.
* As a Site User I can visit an about page so that I can find more information about the site.
* As a Site User I can write a message to a contact form so that I can communicate with the admin.
* As a Site User I can search for a movie so that I can find more about the movie.
* As a Site User I can visit a page so that I can view the top rated movies.
* As a Site User I can view movie details so that I can find more details about the movie.
* As a Site User I can view the most popular movies so that I can discover what movies are trending to watch.
* As a Site User I can view the upcoming movies so that I can discover new movies.
* As a Registered User I can view comments on a movie so that I can read the conversation.
* As a Registered User I can access a webpage where I can comment on a movie so that I can be involved in the conversation.
* As a Registered User I can click to add a movie to my favourites list so that I can have my favourites movies organised.
* As a Registered User I can click to remove a movie from my favourites so that I can update my favourites list.
* As a Registered User I can add rating to a movie so that I can express how much I liked a movie.
* As a Registered User I can delete comments from a movie so that manage the content on the platform more effectively.
* As a Registered User I can edit my comments so that manage the content on the platform more effectively.

## Database Diagram

[Database Diagram](/documentation/wireframes_diagrams/DBdiagram.png)

## Features

All pages on the site are responsive and have :

* ### Navigation Bar

Site user [navbar](/documentation/features/navbar.png) contains the logo (acts as home button), Home, About, Top 15 Movies, Login, Signup and the searh form.

Registered user [navbar](/documentation/features/navbar-reg.png) contains the logo (acts as home button), Home, About, Top 15 Movies, Logout and the searh form.

* [Favicon](/documentation/features/favicon.png)

### Home Page

The [Home Page](/documentation/features/index.png) displays the top 3 rated movies.

### About Page

The [About Page](/documentation/features/about.png) gives information about the website.

### Contact Page

The [Contact Page](/documentation/features/contact.png) contains a contact form.

### Top 15 Movies Page

The [Top 15 Movies Page](/documentation/features/ratings.png) displays the top 15 rated movies.

### Login Page

The [Login Page](/documentation/features/login.png) contains the login form and reset password link.

### Logout Page

The [Logout Page](/documentation/features/logout.png) logout button.

### Signup Page

The [Signup Page](/documentation/features/signup.png) contains the sign up form.

### Favourites Page

Only registered users can visit the favourites page.

The [Favourites Page](/documentation/features/favourites.png) user's favourite movies.

#### Remove Favourite Modal

The [Remove Favourite Modal](/documentation/features/favourites-delete.png) asks the user to confirm movie removal.

### Search Results Page

The [Results Page](/documentation/features/results.png) contains a list of the movies generated from query entered in the search form by the user.

### Movie Details Page

The [Movie Page](/documentation/features/movie.png) contains the following details: poster, title, overview, release date, cast, genres, homeapage, production companies, production countries, spoken languages, original lanaguage, original title, budget, revenue and the runtime. It also displays the rating average(if rated).

The registered user [Movie Page](/documentation/features/add-rating.png) contains also the give rating stars and the add favourites button.

If the registered user give rating to a [Movie](/documentation/features/rated.png) it displays user's rating.

### Comment Page

Only registered users can visit the comment page.

The [Comment Page](/documentation/features/comments.png) contains the movie's poster, title, release date, overview, rating average and gernes on top of the page. Then the comment section where it displays the comments count, text editor, delete and edit buttons for user's own comments

#### Delete Comment Modal

The [Delete Comment Modal](/documentation/features/comments-delete-modal.png) asks the user to confirm comment delete.

### 403 error page

The [403 page](/documentation/features/403.png) displays an image with a text error 403: Forbidden.

### 404 error page

The [404 page](/documentation/features/404.png) displays an image with a text error 404: Not found.

### 405 error page

The [405 page](/documentation/features/error.png) displays an image with a text error.

### 500 error page

The [500 page](/documentation/features/500.png) displays an image with a text : 500 Internal server error.

## Technologies Used

### Languages Used

HTML, CSS, JS, Python

JSON - To serialize movie's data for network transmission between the program and [TMDB API](https://www.themoviedb.org/), and for simplified storage in the database.

### Frameworks, Libraries & Programs Used

* Databases Used
  * [ElephantSQL](https://www.elephantsql.com/)

#### Frameworks Used

* [Django Project](https://www.djangoproject.com/) - A framework to build the app.
* [Bootstrap](https://getbootstrap.com/) - version 4.6.2 - CSS Framework.

#### Libraries Used

* [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/#) - To display the contact form.
* [django-ckeditor](jango-ckeditor.readthedocs.io/en/latest/#toc-entry-1) - As a text editor to the contact form and the comments.
* [Gunicorn](https://gunicorn.org/) - As the server for Heroku.
* [Dj_database_url](https://pypi.org/project/dj-database-url/) - To parse the database URL from the environment variables in Heroku.
* [Psycopg2](https://pypi.org/project/psycopg2/) - As an adaptor for Python and PostgreSQL databases.
* [Allauth](https://docs.allauth.org/en/latest/installation.html) - For authentication, registration, account management.
* [jQuery](https://jquery.com/) - A JavaScript library to handle front end functions.
* [Cloudinary](https://cloudinary.com/) - To host images

#### Programs Used

* [TMDB API](https://www.themoviedb.org/) - API to get the movie details.
* [GitHub](https://github.com/) - To save and store files for the website.
* [VSCode](https://code.visualstudio.com/) - Code editor used for local development.
* [GitPod](https://gitpod.io/) - IDE used to create the site.
* [Balsamiq](https://balsamiq.com/) - Used to create wireframes.
* [DBdiagram](/https://dbdiagram.io/home) - To create database diagrams.
* [Techsini](https://techsini.com/multi-mockup/index.php) - To display the web image in various devices.
* [Google Developer Tools](https://developer.chrome.com/docs/) - To test features, resposiveness and stylilng.
* [TinyPNG](https://tinypng.com/) - To reduce size of the images.
* [Favicon](https://favicon.io/) - To create favicon.
* [Shields IO](https://shields.io/) - To add badges to README.
* [Obsidian](https://code.visualstudio.com/) - To keep notes.

## Deployment and Local Development

### Local Development

When in development navigate to the settings.py and change the following variables to:

* To view code errors

```python
DEBUG = True
```

* To view emails in the terminal

```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

* To set the staticfiles storage

```python
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
```

#### How to fork

To fork the repository :

1. Log in (sign up) to GitHub.
2. Go to the repository for this project [MovieHub](https://github.com/Vasileios20/MovieHub).
3. Click the fork button in the top right corner.

#### How to clone

To clone the repository :

1. Log in (sign up) to GitHub.
2. Go to the repository for this project [MovieHub](https://github.com/Vasileios20/MovieHub).
3. Click on the code button, select one of the HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.

### Deployment

The site has been deployed using Heroku. Deployed site [VastMovieHub](https://moviehub-vas-2ed6679610a9.herokuapp.com). Follow these steps:

#### ElephantSQL

If you don't already have an account to ElephantSQL, create one [here](https://www.elephantsql.com).

* Create an external database with

  * Log into ElephantSQL
  * Click "Create New Instance"
  * Set up a plan by giving a Name and selecting a Plan
  * Click "Select Region" and choose a Data center
  * Click "Review", check all details and click "Create Instance"
  * Return to the Dashboard and click on the database instance name
  * Copy the database URL

#### Heroku App

If you don't already have an account to Heroku, create one [here](https://www.heroku.com/).

* Create Heroku app
  * Go to the Heroku dashboard and click the "Create new app" button.
  * Name the app. Each app name on Heroku has to be unique.
  * Then select your region.
  * And then click "Create app".

#### Attach the Database

* In the IDE file explorer or terminal
  * Create new env.py file on top level directory

* In env.py
  * Import os library
  * Set environment variables
  * Add database url
  * Add in secret key
  * Add TMDB API KEY
  * Add email address
  * Add email password

```python
import os

os.environ["DATABASE_URL"] = "Paste in ElephantSQL database URL"    
os.environ["SECRET_KEY"] = "Make up your own randomSecretKey"    
os.environ["TMDB_API_KEY"] = "Your TMDB API key"    
os.environ["EMAIL_ADDRESS"] = "Your email address"
os.environ["EMAIL_PASSWORD"] = "Your email password"
os.environ["CLOUDINARY_URL"] = "Paste in the API Environment variable"
```
  
If you don't already have an account to Cloudinary, create one [here](https://cloudinary.com/).

* Cloudinary
  * Go to the Cloudinary dashboard and copy the API Environment variable.
  * Paste in env.py variable CLOUDINARY_URL(see above)
  
* In heroku app
  * Go to the settings tab.
  * In the settings click the button "Reveal Config Vars".
  * Click Add and use

    |KEY|VALUE|
    |--|--|
    |PORT|8000|
    |DATABASE_URL|Paste in ElephantSQL database URL|
    |SECRET_KEY|Your own randomSecretKey|
    |TMDB_API_KEY|Your TMDB API key|
    |EMAIL_ADDRESS|Your email address|
    |EMAIL_PASSWORD|Your email password|
    |CLOUDINARY_URL|Paste in the API Environment variable|

  * Go to the deploy tab.
  * Choose the deployment method.
  * Select Github, and confirm to connect to Github.
  * Search for the Github repository name.
  * Then click "connect".
  * Scroll down and click "Deploy Branch".

## Testing

Please see [Testing](TESTING.md)

## Credits

"This website uses [TMDB](https://www.themoviedb.org/) and the TMDB APIs but is not endorsed, certified, or otherwise approved by TMDB."

### Code Used

[Code Institute's](https://codeinstitute.net/) - Walkthrough project I Think Therefore I Blog

[Youtube Tutorial](https://www.youtube.com/watch?v=tm9Yps3IkmQ&list=PLBQzvdjNG8c-g_mVYUNiVDwwO5YgcbNwT&index=1) - To fetch data from the TMDB API.

[dev](https://dev.to/ieeecsvitc/integrating-rich-text-editor-with-django-k19) - Integrating Rich Text Editor with Django

[codepen](https://codepen.io/GeoffreyCrofte/pen/ALOggg) - To display stars to give rating.

[codepen](https://codepen.io/Bluetidepro/pen/AGXMMp) - To display movie rating with stars.

[Stack overflow](https://stackoverflow.com/questions/59593884/django-rendering-a-number-as-a-5-stars-rating) - Star rating

[Youtube Tutorial by Pyplane](https://www.youtube.com/watch?v=iz1GB_q5txM) - To get user rating choice and send data to the server

[mailtrap](https://mailtrap.io/blog/django-contact-form/) - To create contact form and connect it with the database and send email to admin.

[Stack Overflow](https://stackoverflow.com/questions/39088813/django-paginator-with-many-pages) - To display set of pages in pagination

[Stack Overflow](https://stackoverflow.com/) and [Django Documentation](https://docs.djangoproject.com/en/4.2/) were consulted during the whole project for various issues I faced, both front end and back end

### Media

[No image available](https://commons.wikimedia.org/wiki/File:No-Image-Placeholder.svg) - To use it as a placeholder when movie doesn't contain poster

### Aknowledgments
