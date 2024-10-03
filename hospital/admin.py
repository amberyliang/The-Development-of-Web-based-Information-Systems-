from django.contrib import admin
from hospital import models


# Register your models here.
class AnnouncementAdmin(admin.ModelAdmin):
	list_display = ('title' , 'content', 'pub_time') 
	ordering = ('-pub_time',)

class DepartmentAdmin(admin.ModelAdmin):
	list_display = ('name','description') 

class DoctorAdmin(admin.ModelAdmin):
	list_display = ('name' , 'bio','department')

class RegistrationAdmin(admin.ModelAdmin):
	list_display = ('name' , 'birthday','gender','id_number','phone_number','date','department') 

class EmailReceiveAdmin(admin.ModelAdmin):
	list_display = ('name','email','subject','message')

class UserAdmin(admin.ModelAdmin):
	list_display = ('name','email','birthday','phone_number','password')

class AppointmentAdmin(admin.ModelAdmin):
	list_display = ('name','department','email','phone_number','date')
	

admin.site.register(models.Announcement,AnnouncementAdmin)
admin.site.register(models.Department,DepartmentAdmin)
admin.site.register(models.Doctor,DoctorAdmin)
admin.site.register(models.Registration,RegistrationAdmin)
admin.site.register(models.Emailreceive,EmailReceiveAdmin)
admin.site.register(models.User,UserAdmin)
admin.site.register(models.Appointment,AppointmentAdmin)