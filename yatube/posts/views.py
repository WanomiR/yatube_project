from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Main page")


def group_posts(request, pk: int):
    return HttpResponse(f"Group number {pk}")