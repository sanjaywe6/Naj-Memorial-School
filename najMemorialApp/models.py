from distutils.command.upload import upload
from django.db import models
from sqlalchemy import true
from django.db import models

# Create your models here.
class Gallary(models.Model):
    img_id=models.AutoField(primary_key=true)
    img=models.ImageField(upload_to='najmemorial/gallary')
    img_date=models.DateField()

class frontImg(models.Model):
    img_id=models.AutoField(primary_key=true)
    img=models.ImageField(upload_to='najmemorial/frontImg')

class Contact(models.Model):
    cont_id=models.AutoField(primary_key=true)
    cont_name=models.CharField(max_length=50)
    cont_email=models.CharField(max_length=50)
    cont_phone=models.CharField(max_length=20,default="")
    cont_desc=models.CharField(max_length=500)

    def __str__(self):
        return self.cont_name

class Commentq(models.Model):
    comm_id=models.AutoField(primary_key=true)
    comm_name=models.CharField(max_length=30,default="Unknown")
    comm_sub=models.CharField(max_length=50,default="Not Categorize")
    comm_desc=models.CharField(max_length=500)
    comm_date=models.DateField()

    def __str__(self):
        return self.comm_name

#  modal for verifying autobots
class verify_bot(models.Model):
    sno=models.AutoField(primary_key=True)
    img=models.ImageField(upload_to='najmemorial/verify_bot')
    value=models.IntegerField()
