from django.urls import URLPattern, include, path
from . import formViews
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

urlpatterns = [
    path('createEvent', formViews.createEvent),
    path('deleteEvent', formViews.deleteEvent),
    path('getEvents', formViews.getEvents),
    path('getAllEvents', formViews.getAllEvents),
    path('getEvent', formViews.getEvent),
    path('saveEvent', formViews.saveEvent),
    path('registerEvent', formViews.registerEvent),
    path('sendOtp',formViews.sendOtp),
    path('verifyOtp',formViews.verifyOtp),
    path('getAllCandidates',formViews.getAllCandidates)
]
