from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'core/index.html')


def topic_details(request, pk):
    return render(request, 'core/topic_details.html')
