"""
Definition of urls for restApi.
"""

from django.urls import path
from . import views


urlpatterns = [
    path('getData',views.getData),
    path('saveData',views.saveData),
    ]