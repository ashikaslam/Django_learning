from django.contrib import admin

# Register your models here.
from . import models
class  User_admin(admin.ModelAdmin):
    list_display=['mobile_number','email','name']


admin.site.register(models.User,User_admin)