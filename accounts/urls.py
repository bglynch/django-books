# accounts url.py

from django.conf.urls import url
from accounts.views import login, register


urlpatterns = [
    url(r'^login', login, name='login'),
    url(r'^register$', register, name='register'),
]
