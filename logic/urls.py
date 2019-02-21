from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('course',views.CourseViewSet)
router.register('prerequisite',views.PrerequisiteViewSet)

urlpatterns = [
    path('',include(router.urls))
]