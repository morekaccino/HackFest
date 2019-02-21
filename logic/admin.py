from django.contrib import admin
from logic.models import *


# Register your models here.

class FacultyAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ['name']


class ProgramAdmin(admin.ModelAdmin):
    list_display = ("name", "faculty",)
    search_fields = ['name', "faculty"]


class CourseAdmin(admin.ModelAdmin):
    list_display = ("name",
                    "code",
                    "faculty",
                    "credit",
                    "lang",
                    "about",)
    search_fields = ["name",
                     "code",
                     "faculty",
                     "credit",
                     "lang",
                     "about"]


class PrerequisiteAdmin(admin.ModelAdmin):
    list_display = ("pre", "post","alt")
    search_fields = ["pre", "post","alt"]


admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Prerequisite, PrerequisiteAdmin)
