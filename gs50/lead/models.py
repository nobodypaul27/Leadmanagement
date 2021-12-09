from django.db import models
from django.contrib.auth.models import User
from django.http import request



# Create your models here.
class Lead(models.Model):
    name= models.CharField(max_length=200)
    company_name = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        ordering = ['-name',]



#Lead.objects.filter(user=request.user)




