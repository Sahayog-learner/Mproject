from django.db import models

# Create your models here.
class Logins(models.Model):
   name=models.CharField(null=True,max_length=120)
   email=models.CharField(max_length=120)
   phone=models.CharField(unique=True,null=True,max_length=12)
   

   def __str__(self) :
      return self.name