from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import (
        HttpResponse, HttpResponseNotFound, HttpResponsePermanentRedirect,
        Http404
    )


def index(request):
    return HttpResponse("The women's page")

def categories(request, cat_id):
    return HttpResponse(f"<h1>Articles by categories</h1><h2>id: {cat_id}</h2>")

def categories_by_slug(request, cat_slug):
    return HttpResponse(f"<h1>Articles by slug</h1><h2>{cat_slug}</h2>")

def archive(request, year):
    if year > 2024:
        uri = reverse('cats', args=('music',))
        return HttpResponsePermanentRedirect(uri)
    return HttpResponse(f"<h1>Archive by year </h1><h2>{year}</h2>")

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Oops! Page not Found</h1>")