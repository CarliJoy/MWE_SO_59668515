

import coreapi
import io

from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from Usersapi.models import UserReceived


def home(request):
    client = coreapi.Client()
    data = client.get('http://127.0.0.1:8000/api/usersapi/1/')

    name = data.get("name")
    age = data.get("age")
    gender = data.get("gender")
    user = UserReceived.objects.create(name=name, age=age, gender=gender)
    user.save()

    return HttpResponse(f"OKAY, got and saved user {name}")
