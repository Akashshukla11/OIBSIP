from django.db import models

class employees(models.Model):
    name = models.CharField(max_length=100)
    email = models.TextField()
    address = models.TextField()
    phone = models.IntegerField()

    def __str__(self):
        return self.name
