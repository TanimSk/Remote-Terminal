from django.shortcuts import render
from django.http import HttpResponse
import json


def home(req):
    if req.method == 'POST':
        data = json.loads(req.body)
        try:
            # print(data['uuid'])
            return render(req, 'terminal.html')

        except KeyError:
            return HttpResponse(False)
            
        return HttpResponse(False)

    return render(req, 'home.html')


def upload_file(req):
    if req.method == 'POST':
        pass
    else:
        return HttpResponse(False)


def documentation(req):
    return render(req, 'doc.html')