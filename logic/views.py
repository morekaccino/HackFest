from django.shortcuts import render, HttpResponse
from logic.inseringToDB import inserting
from logic.prerequisite import prerequisite
from _thread import start_new_thread
from rest_framework import viewsets
from logic.models import *
from logic.serializer import *


# Create your views here.

def modification(request):
    mandatory = [
        "EECS 1001",
        "EECS 1012",
        "EECS 1019",
        "EECS 1022",
        "EECS 2001",
        "EECS 2011",
        "EECS 2021",
        "EECS 2030",
        "EECS 2031",
        "EECS 3101",
        "EECS 3311",
        # "MATH 1090",
        # "MATH 1300",
        # "MATH 1310",
    ]
    all_courses = Course.objects.all()
    for course in all_courses:
        if " " in course.code:
            course.code = course.code.replace(" ", "")
            course.save()

    return HttpResponse("Done")


def insert(request):
    inserting()
    return HttpResponse("Done")


def prerequisiteView(request):
    prerequisite()
    return HttpResponse("Done")


class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class PrerequisiteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Prerequisite.objects.all()
    serializer_class = PrerequisiteSerializer
