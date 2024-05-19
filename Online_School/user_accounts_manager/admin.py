from django.contrib import admin
from rest_framework import status
from rest_framework.response import Response
# Register your models here.
from . import models
class  User_admin(admin.ModelAdmin):
    list_display=['mobile_number','email','name']


admin.site.register(models.User,User_admin)




# instructor


class ApplicationsForinstructorsAdmin(admin.ModelAdmin):
    # def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
    #    queryset = super().get_queryset(request)
    #    return queryset.filter(aproved=False)
    list_display=['user','aproved']
    def save_model(self, request, obj, form, change):
        if form.cleaned_data['aproved']:
            try:
                user = obj.user
                models.InstructorsProfile.objects.create(
                user=user,
                name=obj.name,
                phone_number=obj.phone_number,
                email=obj.email,
                gender=obj.gender,
                educations=obj.educations,
                state=obj.state,
                city=obj.city,
                country=obj. country,
                )
                if user.account_type == 'student':user.account_type = 'instructors'
                elif user.account_type == 'administrator':user.account_type = 'administrator_instructor'

                user.profile_picture = 'static_files/images/teacher_image.jpeg'
                user.save()
            except Exception as e:return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)  
        super().save_model(request, obj, form, change)
        obj.delete()
admin.site.register(models.ApplicationsForinstructors,ApplicationsForinstructorsAdmin)


class instructorsAdmin(admin.ModelAdmin):
    list_display=['name','phone_number']


admin.site.register(models.InstructorsProfile,instructorsAdmin)

