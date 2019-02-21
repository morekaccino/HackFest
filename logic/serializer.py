from django.contrib.auth.models import User, Group
from logic.models import *
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('pk',
                  'name',
                  'code',
                  'nickname',
                  'faculty',
                  'credit',
                  'lang',
                  'about',)


class PrerequisiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prerequisite
        fields = ('pk', 'pre', 'post','alt')
