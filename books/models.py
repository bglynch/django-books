# books/model.py

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    name    = models.CharField(max_length=254, default='')
    author  = models.CharField(max_length=254, default='')
    isbn    = models.CharField(max_length=254, default='')
    notes   = models.TextField()
    image = models.ImageField(upload_to='images', default='images/default.png')
    owner = models.ForeignKey(User, related_name='books', null=False)
    
    def __str__(self):
        return self.name
    
