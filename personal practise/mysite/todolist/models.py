from django.db import models
from datetime import date

# Create your models here.

class user(models.Model):
    uid = models.AutoField
    username = models.CharField(max_length=50, default="")
    fname = models.CharField(max_length=50,default="")
    lname = models.CharField(max_length=50,default="" )
    email = models.CharField(max_length=100,default="")
    password = models.CharField(max_length=100,default="")
    def __str__(self):
        return self.fname
class todo(models.Model):
    tid = models.AutoField
    fname = models.CharField(max_length=50,default="")
    uid = models.IntegerField(max_length=50,default="")
    tname = models.CharField(max_length=500,default="")
    task = models.CharField(max_length=500,default="")
    status = models.CharField(max_length=500,default="")
    #tdate = models.DateField()
    def __str__(self):
        return  self.tname

class donetask(models.Model):
    fname = models.CharField(max_length=50,default="")
    uid = models.IntegerField(max_length=50,default="")
    dtid = models.AutoField
    tname = models.CharField(max_length=500,default="")
    task = models.CharField(max_length=500,default="")
    status = models.CharField(max_length=50, default="Completed")
    tdate = models.DateField()
    def __str__(self):
        return self.tname

class notice(models.Model):
    uid = models.IntegerField()
    nid = models.AutoField
    username = models.CharField(max_length=50)
    notice_title = models.CharField(max_length=100)
    notice = models.CharField(max_length=1000)
    notice_date = models.DateField()
    expiry_date = models.DateField()
    completion_date = models.DateField()
    def __str__(self):
        return self.username