from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views import View
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from formdum.forms import DummForm
from formdum.schemas import REVIEW_SCHEMA, ReviewSchema
from marshmallow.exceptions import ValidationError as MarshError


# Create your views here.
class FormDummView(View):
    def get(self, request):
        form = DummForm()
        return render(request, 'form.html', context={
            'form': form
        })

    def post(self, request):
        form = DummForm(request.POST)
        if form.is_valid():
            context = form.cleaned_data
            return render(request, 'form.html', context)
        else:
            return render(request, 'error.html', {'errors': form.errors})


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
