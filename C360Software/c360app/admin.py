from django.contrib import admin

from .models import Patient,Employee,Attendance

# Register your models here.
# 
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name','gender','address')   
    list_per_page = 4
   

class EmpoyeeAdmin(admin.ModelAdmin):
    list_display = ('id','firstname')

admin.site.register(Patient,PatientAdmin)
admin.site.register(Employee,EmpoyeeAdmin)
admin.site.register(Attendance)



