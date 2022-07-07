from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404


def index(request):
    return HttpResponse("Страница приложения Women")


def categories(request, cat):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1> <p>{cat}</p>")


def archive(request, year):
    if int(year) > 2020:
        return redirect('/', permanent=True)
    return HttpResponse(f"<h1>Архив по годам</h1> <p>{year}</p>")


def page_not_found(request, exeption):
    return HttpResponseNotFound("Страница не найдена")
