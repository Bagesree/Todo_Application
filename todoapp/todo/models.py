from django.db import models


# Create your models here.

# class login(models.Model):
#     username = models.CharField(max_length=250)
#     password = models.CharField(max_length=150)
#     email = models.EmailField(max_length=300)
#     age = models.IntegerField(default=1,blank=True,null=True)

class Tasks(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default='')
    completed = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class login(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=150)


class Register(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
