from django.db import models

class Employees(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=70)

    def __str__(self):
        return self.name