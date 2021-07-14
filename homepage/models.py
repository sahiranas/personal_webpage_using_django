from django.db import models
from django.db.models.fields import CharField, TextField


# Create your models here.
class Education(models.Model):
    heading = models.CharField(max_length=50)
    board = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    stream = models.CharField(max_length=70)
    cgpa = models.FloatField()
    year = models.CharField(max_length=10)


class PythonProjects(models.Model):
    collapseid=models.CharField(default='a',max_length=5) #provided to proper collapse of each sub sections
    heading=models.CharField(max_length=100)
    description=models.TextField()
    gitlink=models.CharField(max_length=250)

class WebProject(models.Model):
    collapseid=models.CharField(default='a',max_length=5) #provided to proper collapse of each sub sections
    heading=models.CharField(max_length=100)
    description=models.TextField()
    gitlink=models.CharField(max_length=250)


