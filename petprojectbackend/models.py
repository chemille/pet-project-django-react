from django.db import models

class Pet(models.Model): # This is how django knows it's a model
    # Give it a data type
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name + ' ' + self.description