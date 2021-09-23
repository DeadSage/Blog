from django.contrib import admin
from django.urls import include, path

from formdum import views
from core.views import index, topic_details

urlpatterns = [
    path('', views.SchemaView.as_view()),
]
