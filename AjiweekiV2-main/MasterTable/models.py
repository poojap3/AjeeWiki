from django.db import models

# Create your models here.


class QuestionType(models.Model):
    # id=models.CharField(max_length=50, null=True, blank=True)
    name=models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

    
