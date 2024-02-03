from django.contrib import admin
from.import models
# Register your models here.

#admin.site.register(models.Book)


class book_show(admin.ModelAdmin):
    list_display = ('id','name','first_pub','last_pub')


admin.site.register(models.Book,book_show)