from django.contrib import admin

# Register your models here.

from.models import ContactUs

class ContactModelAdmin(admin.ModelAdmin):
    list_display=['name','phone']


admin.site.register(ContactUs,ContactModelAdmin)