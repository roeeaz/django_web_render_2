from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='Posted_Images')

    def __str__(self):
        return self.title


class Student(models.Model):
    user =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    sname = models.CharField(max_length=100)
    age = models.IntegerField()
    img = models.ImageField(upload_to='Posted_Images')

    def __str__(self):
        return self.sname
