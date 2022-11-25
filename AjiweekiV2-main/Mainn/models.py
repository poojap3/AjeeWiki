from django.db import models
from django.contrib.auth.models import User
from Account.models import *
from MasterTable.models import *


# Model for store Form details.

class Form(models.Model):
    name=models.CharField(max_length=2000, null=True, blank=True)
    description=models.CharField(max_length=2000, null=True, blank=True)
    category_name=models.CharField(max_length=2000,null=True,blank=True)

    def __str__(self):
        return self.name

# Model for store Questions details.

class Questions(models.Model):
    form=models.ForeignKey(Form,null=True, on_delete= models.CASCADE)
    question_type=models.ForeignKey(QuestionType,null=True, on_delete= models.CASCADE)
    elements=models.CharField(max_length=2000, null=True, blank=True)
    multiple_option=models.BooleanField(max_length=2000, null=True, blank=True)

    name=models.CharField(max_length=2000, null=True, blank=True)
    is_required=models.CharField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.name


#  Model for store QuestionChoice details.

class QuestionChoice(models.Model):
    question=models.ForeignKey(Questions,null=True, on_delete= models.CASCADE)
    name=models.CharField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.name

#  Model for store QuestionChoice details.

class UserResponse(models.Model):
    user = models.ForeignKey(CustomUser,null=True, on_delete= models.CASCADE)
    question=models.ForeignKey(Questions,null=True, on_delete= models.CASCADE,related_name='question')
    answer=models.TextField(max_length=2000, null=True, blank=True)
    # question_id=models.CharField(max_length=2000, null=True, blank=True)
    # user_id=models.CharField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.answer
