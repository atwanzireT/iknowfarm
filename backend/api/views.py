from email import header
from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.
def api_view(request, *args, **kwargs):
    # request body
    body = request.body # Byte string of Json data
    print(body)
    data = {}

    try:
        data = json.loads(body)
    except:
        pass

    print(data)
    print(request.headers)
    # data['headers'] = request.headers
    return JsonResponse({"message":"Hey there this is your django api reponse"})