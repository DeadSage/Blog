from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from feedback.forms import DummForm
from feedback.schemas import REVIEW_SCHEMA, ReviewSchema
from django.contrib.auth.mixins import LoginRequiredMixin
from marshmallow.exceptions import ValidationError as MarshError
from .models import Feedback


# Create your views here.
class FeedbackCreateView(LoginRequiredMixin, CreateView):
    model = Feedback
    fields = ['text', 'grade', 'subject']
    success_url = '/feedback/add'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class FeedbackListView(LoginRequiredMixin, ListView):
    model = Feedback

    def get_queryset(self):
        if self.request.user.is_staff:
            return Feedback.objects.all()
        return Feedback.objects.filter(author=self.request.user)

class SchemaView(View):
    def post(self, request):
        try:
            document = json.loads(request.body)
            validate(document, REVIEW_SCHEMA)
            return JsonResponse(document, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'errors': 'Invalid JSON'}, status=400)
        except ValidationError as exc:
            return JsonResponse({'errors': exc.message}, status=400)


class MarshView(View):
    def post(self, request):
        try:
            document = json.loads(request.body)
            schema = ReviewSchema(strict=True)
            data = schema.load(document)
            return JsonResponse(data, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'errors': 'Invalid JSON'}, status=400)
        except MarshError as exc:
            return JsonResponse({'errors': exc.messages}, status=400)
