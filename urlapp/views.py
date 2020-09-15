from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect
from .models import UrlEntry

# Create your views here.


def index(request):
    return render(request, 'index.html')


def shorten_url(request) -> HttpResponse:
    if request.method == "GET":
        incoming = request.GET

        if incoming.get('base_url'):
            base_url = incoming.get('base_url')

            # if URL doesnt already exist in database, create new
            if UrlEntry.objects.filter(full_url=base_url).exists() == False:
                url = UrlEntry(full_url=base_url)
                url.save()

            return JsonResponse({
                'url': request.get_host() + "/" + UrlEntry.objects.filter(full_url=base_url).last().url_hash
            }, status=200)


def root(request, url_hash):
    url = get_object_or_404(UrlEntry, url_hash=url_hash)
    return redirect(url.full_url)
