from django.shortcuts import render


def index(request):
    return render(request, 'one/index.html', {})
# Create your views here.
def sample(request):
    return render(request, 'one/sample.html', {})

def about(request):
    return render(request, 'one/about.html', {})

def event_calendar(request):
    return render(request, 'one/event_calendar.html', {})

def news(request):
    return render(request, 'one/news.html', {})

def gallery(request):
    return render(request, 'one/gallery.html', {})

def contact(request):
    return render(request, 'one/contact.html', {})


def member_page(request):
    return render(request, 'one/member_page.html', {})