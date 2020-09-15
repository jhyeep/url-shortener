# URL Shortener

A simple URL shortener web app made with Django. Deployed on http://jh3.herokuapp.com/.

## More Info

The shortener takes in a URL input, hashes it and saves both the URL and the hash as an entry in a Postgres database. 

The shortened link is displayed as [domain]/[hash]. Accessing the link will redirect the user to the corresponding URL, based on the hash.

## Important Files
* **urlapp/models.py**: Fields for database entries

* **urlapp/views.py**: API

* **urlapp/static/scripts.js**: JQuery code for frontend

* **urlshortener/urls.py**: URL paths

* **tests.py**: Unit tests - run using python manage.py test