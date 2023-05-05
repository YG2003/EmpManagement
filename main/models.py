from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employee(models.Model):
    company = models.ForeignKey(User, on_delete = models.CASCADE)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    role = models.CharField(max_length = 100, default = 'Not Assigned')
    dept = models.CharField(max_length = 100, default = 'Not Assigned')
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()

    def __str__(self):
        return "%s %s" %(self.first_name, self.last_name)