from django.contrib import admin
from django.urls import include, path
from core.views import index, topic_details
from feedback.views import FeedbackCreateView

urlpatterns = [
    path('add', FeedbackCreateView.as_view(), name='feedback-create'),
]
