from django.shortcuts import render
from django.http import HttpResponse
import json


def home(req):
    if req.method == 'POST':
        data = json.loads(req.body)
        try:
            print(data['uuid'])
            return HttpResponse('OK')

        except KeyError:
            return HttpResponse('ERROR')

        return HttpResponse('ERROR')

    return render(req, 'home.html')
