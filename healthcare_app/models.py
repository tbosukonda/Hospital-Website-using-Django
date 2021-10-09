from django.db import models

class DoctorModel(models.Model):
    name = models.CharField(max_length=10)
    speciality = models.CharField(max_length = 10)
    schedule = models.CharField(max_length=10)

class CustomerModel(models.Model):
    userid = models.CharField(max_length = 10)
    speciality = models.CharField(max_length=10)
    contactno = models.CharField(max_length=10)

class BookapptModel(models.Model):
    username = models.CharField(max_length=10)
    contactno = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    speciality = models.CharField(max_length=10)
    schedule = models.CharField(max_length=10)
    status = models.CharField(max_length=10)