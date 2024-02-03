from django.contrib import admin
from .import models
# Register your models here.

class show_st(admin.ModelAdmin):
    list_display = ('roll','name','addr')

class show_te(admin.ModelAdmin):
    list_display = ('name','addr')

admin.site.register(models.Student,show_st)
admin.site.register(models.Teacher,show_te)


@admin.register(models.Employee)
class x(admin.ModelAdmin):  # i can name the class anything
    list_display = ('name','addr')



@admin.register(models.Maneger)
class y(admin.ModelAdmin):  # i can name the class anything
    list_display = ('name','addr')




class show_Me(admin.ModelAdmin):
    list_display = ('roll','name')

class show_f(admin.ModelAdmin):
    list_display = ('roll','name')


admin.site.register(models.Friends,show_f)
admin.site.register(models.Me,show_Me)


class show_p(admin.ModelAdmin):
    list_display = ('name','age',)
    
class show_pas(admin.ModelAdmin):
    list_display = ('user_id','pasNUM',)



admin.site.register(models.People,show_p)
admin.site.register(models.Passport,show_pas)
admin.site.register(models.Post)


class show_stu(admin.ModelAdmin):
    list_display = ('name','roll',)

class show_tc(admin.ModelAdmin):
    list_display = ('name','sub','stu_List')

admin.site.register(models.Stu,show_stu)
admin.site.register(models.Tec,show_tc)

