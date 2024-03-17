from django.db import models

# Create your models here.
class Pet(models.Model):
    name=models.CharField(max_length=20,null=True)
    description = models.TextField()
    healthcondition = models.TextField()
    image=models.ImageField(null=True,blank=False)
    
    objects = models.Manager()
    
    def __str__(self):
        return f'{self.name}'
    
    
    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url
        
class Name(models.Model):
    name=models.CharField(max_length=20)