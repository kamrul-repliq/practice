from django.db import models

# Create your models here.

class Fruits(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    kind = models.CharField(max_length=100,blank=True,null=True)
    
    def __str__(self):
        return f"{self.name}"