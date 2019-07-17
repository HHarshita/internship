from django.db import models


class register(models.Model):
    fname=models.CharField(max_length=20)
    lname= models.CharField(max_length=20)
    gender= models.CharField(max_length=10)
    dob=models.DateTimeField(max_length=30)
    email=models.CharField(max_length=20)
    password = models.CharField(max_length=10)
    cpassword = models.CharField(max_length=10)
    domain = models.CharField(max_length=50)
    address= models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    country=models.CharField(max_length=20)