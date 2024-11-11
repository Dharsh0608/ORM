from django.db import models

# Create your models here.
from django.db import models
from django.contrib import admin
class Bank(models.Model):
  name=models.CharField (max_length=100)
  accountnumber=models.IntegerField()
  amount=models.IntegerField()
  income=models.IntegerField()
  security=models.CharField(max_length=6)
  intrest=models.IntegerField()
  

class BankAdmin(admin.ModelAdmin):
  list_display=('name','accountnumber','amount','income','security','intrest')


