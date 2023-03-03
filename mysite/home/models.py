from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=12)
    address = models.CharField(max_length=120)
    details = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.name