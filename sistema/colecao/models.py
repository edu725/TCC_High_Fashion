from django.db import models
from users.models import User

# Create your models here.
class Collection(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='img/%Y/%m/%d/')

    def __str__(self):
        return self.name