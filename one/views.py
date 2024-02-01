from django.shortcuts import render


def index(request):
    return render(request, 'one/index.html', {})
# Create your views here.
