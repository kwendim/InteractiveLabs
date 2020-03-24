from django.contrib import admin

from .models import *

admin.site.register(Courses)
admin.site.register(Labs)
admin.site.register(CourseOwnership)
admin.site.register(Grades)
admin.site.register(CourseToLab)
# Register your models here.
