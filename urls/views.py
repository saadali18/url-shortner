from django.shortcuts import render, redirect
from .models import Url
from django.http import HttpResponse
from .utils import generate_short_url

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        long = request.POST['link']
        url, created = Url.objects.get_or_create(long=long)
        if created:
            short = generate_short_url(url.long)
            url.short = short
            if not url.is_unique:
                while not url.is_unique:
                    short = generate_short_url(url.long)
                    url.short = short
            url.save()

        return HttpResponse(url.short)

def get(request, pk):
    url = Url.objects.get(short=pk)
    return redirect(url.long)


