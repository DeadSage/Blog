from django.contrib import admin
from django.urls import include, path
from core.views import index, topic_details
from formdum.views import MarshView

urlpatterns = [
    path('', MarshView.as_view()),
]
