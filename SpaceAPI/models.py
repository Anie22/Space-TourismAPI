from django.db import models

# Create your models here.

class destination(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='photos')
    description = models.CharField(max_length=500)
    distance = models.CharField(max_length=100)
    travel = models.CharField(max_length=40)

    def __str__ (self):
        return self.name

class crew(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField()
    role = models.CharField(max_length=40)
    bio = models.CharField(max_length=500)

    def __str__ (self):
        return self.name

class technology(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField()
    description = models.CharField(max_length=500)

    def __str__ (self):
        return self.name
