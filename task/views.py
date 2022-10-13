from django.http import HttpResponse
from .UniversityID import UniversityID


def id_validator(request, ID):
    try:
        id = UniversityID(ID)
    except:
        return HttpResponse("Not a Valid ID :(")
    return HttpResponse("Valid ID, Entrance Year is " + str(id.components['classYear']))


def index(request):
    return HttpResponse("Hello There... Please add \"/YourID\" to the URL to Validate it")
