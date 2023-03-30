from django.db import models

# Create your models here.

class Tienda(models.Model):
    headline=models.CharField(max_length=200)
    body=models.TextField()
    image=models.ImageField(upload_to='tienda/images/')
    precio=models.IntegerField()
    
    def __str__(self):
        return self.headline
