from django.shortcuts import render
from django.http import HttpResponse
from .models import Data
import json


def home(req):
    if req.method == "POST":
        # data = json.loads(req.body)

        try:
            return render(req, "terminal.html")

        except KeyError:
            return HttpResponse(False)

        # return HttpResponse(False)

    return render(req, "home.html")


def post_data(req):
    if req.method == "POST":
        data = json.loads(req.body)
        Data.objects.create(text=data.get("data"))
        return HttpResponse("OK")


def documentation(req):
    return render(req, "doc.html")


def download(req):
    return render(req, "download.html")


def about(req):
    return render(req, "about.html")
