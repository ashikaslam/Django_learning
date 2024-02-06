from django.contrib import admin
from.import models
# Register your models here.


class Show(admin.ModelAdmin):
    list_display = ('id','book_name','first_pub','last_pub')


admin.site.register(models.Book,Show)