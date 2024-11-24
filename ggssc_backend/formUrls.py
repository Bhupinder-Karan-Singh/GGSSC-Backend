from django.urls import URLPattern, include, path
from . import formViews
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

urlpatterns = [
    path('createEvent', formViews.createEvent),
    path('getEvents', formViews.getEvents),
]
