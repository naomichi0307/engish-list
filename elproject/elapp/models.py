from django.db import models

# Create your models here.

PRIORITY=(('danger','high'),('info','middle'),('success','low'))
class elModel(models.Model):
    word=models.CharField(max_length=25)
    #mean=models.CharField(max_length=100)
    priority= models.CharField(
        max_length=50,
        choices = PRIORITY

    )

    duedate=models.DateField()
    def __str__(self):
        return self.word
