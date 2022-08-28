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
    #mean = models.CharField(max_length=100)
    duedate=models.DateField()
    def __str__(self):
        return self.word

class Newword(models.Model):
    word = models.CharField(max_length=25)
    date = models.DateField()

    def  __str__(self):
        return self.word