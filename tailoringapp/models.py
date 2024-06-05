from django.db import models
from django.urls import reverse
# Create your models here.

class Customers(models.Model):

    name = models.CharField(max_length=255, null =True, blank=True)
    size = models.CharField(max_length=255, null =True, blank=True)
    phone = models.CharField(max_length=100, null =True, blank=True)

    def __str__(self):
        return self.name
                
    def get_absolute_url(self):
         #   return reverse('articel_detail', args=(str(self.id)))
             return reverse('home')
    