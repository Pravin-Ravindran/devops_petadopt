"""
This module contains definitions for database models.
"""
from django.db import models

# Create your models here.
class Pet(models.Model):
    """
    Model representing a pet.

    Attributes:
    name (str): The name of the pet.
    description (str): The description of the pet.
    healthcondition (str): The health condition of the pet.
    image (ImageField): The image of the pet.
    """
    name=models.CharField(max_length=20,null=True)
    description = models.TextField()
    healthcondition = models.TextField()
    image=models.ImageField(null=True,blank=False)
    objects = models.Manager()
# Included this  code to display the name alone after saving the pet details
    def __str__(self):
        return f'{self.name}'
    # This code tries to retrieve the url of the image
    @property
    def imageURL(self):
        """
        Model representing a pet.

        Attributes:
        name (str): The name of the pet.
        description (str): The description of the pet.
        healthcondition (str): The health condition of the pet.
        image (ImageField): The image of the pet.
    """
        try:
            url=self.image.url
        except AttributeError:
            url=''
        return url
        