# books url.py

from django.conf.urls import url
from books.views import add_book


urlpatterns = [
    url(r'^addbook', add_book, name='addbook'),

]
