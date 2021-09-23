from django.contrib import admin
from django.urls import include, path
from core.views import index, topic_details
from feedback.views import FeedbackCreateView, FeedbackListView

urlpatterns = [
    path('add', FeedbackCreateView.as_view(), name='feedback-create'),
    path('', FeedbackListView.as_view(), name='feedback-list'),
]
