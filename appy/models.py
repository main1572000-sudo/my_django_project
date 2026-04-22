from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    # image    = models.ImageField(upload_to='photos/%y/%m/%d',null=True)
    def __str__(self):
        return self.username