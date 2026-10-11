from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id=models.AutoField(primary_key=True)
    emp_name=models.CharField(max_length=100)
    emp_email=models.EmailField()
    emp_address=models.CharField(max_length=100)
    emp_designation=models.CharField(max_length=100)
    emp_salary=models.FloatField()
    emp_phone=models.CharField(max_length=10)
