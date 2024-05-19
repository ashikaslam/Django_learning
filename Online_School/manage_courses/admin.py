from django.contrib import admin
from .import models
# Register your models here.


class course_admin(admin.ModelAdmin):
    list_display=['title']


admin.site.register(models.Course,course_admin)