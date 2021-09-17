from django.db import models
from django.db.models import Model
# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name



class Employee(Model):
    id = models.CharField(primary_key=True, max_length=10)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    gender = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)
    address = models.TextField(max_length=800)
    dob = models.DateField()
    date_of_join = models.DateField()
   
    

class Attendance(models.Model):
	emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
	time_stamp = models.DateTimeField()
	photo = models.ImageField(upload_to='detected/', default='c360app/facerec/detected/noimg.png')

	def __str__(self):
		emp = Employee.objects.get(name=self.emp_id)
		return f"{emp.name} {self.time_stamp}"


        
    # def custom_id(self):
    #     return "C36%0" % self.id  