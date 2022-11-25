from django.db import models
from django.contrib.auth.models import User

class CustomUser(models.Model):
    user = models.ForeignKey(User,null=True, on_delete= models.CASCADE)
    user_name = models.CharField(max_length=50, null=True, blank=True)
    email= models.EmailField(max_length=50, null=True, blank=True)
    password=models.CharField(max_length=50, null=True, blank=True)
    phone_number=models.CharField(max_length=50, null=True, blank=True)


    def __str__(self):
        return self.user_name