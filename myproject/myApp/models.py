from django.db import models

# Create your models here.
class EmployeeModel(models.Model):
    eid = models.CharField(max_length=10, primary_key=True)
    ename = models.CharField(max_length=50)
    eemail = models.EmailField()
    eaddress=models.TextField()