from django.contrib import admin
from . import models

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
# Register your models here.

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['appointment_types', 'appointment_status', 'symptom', 'time', 'cancel']
    # def patient_name(self,obj):
    #     return obj.patient.user.first_name
    
    # def doctor_name(self,obj):
    #     return obj.doctor.user.first_name



    def save_model(self, request, obj, form, change):

        if obj.appointment_types=="Online":
            if obj.appointment_status=="Running":
                patient = obj.patient
                email_id = patient.user.email
                confirm_link = f"{obj.doctor.meet_link}"

                email_subject = "meet link"
                email_body = render_to_string('confirm_email.html', {'confirm_link' : confirm_link})
            
                email = EmailMultiAlternatives(email_subject , '', to=[email_id])
                email.attach_alternative(email_body, "text/html")
                email.send()


        
        
            

        super().save_model(request, obj, form, change)
    
admin.site.register(models.Appointment, AppointmentAdmin)