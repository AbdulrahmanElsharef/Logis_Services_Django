from django.db import models
from django.utils.text import slugify

# Create your models here.
class Services(models.Model):
    name=models.CharField( max_length=50)
    title= models.CharField(max_length=200)
    subtitle=models.TextField(max_length=500)
    description=models.TextField(max_length=10000)
    ser_image=models.ImageField(upload_to='Services')
    det_image=models.ImageField( upload_to='Services',blank=True,null=True)
    slug=models.SlugField()
    
    def __str__(self) :
        return str(self.name)
    
    def save(self, *args, **kwargs):
       self.slug=slugify(self.name)
       super(Services, self).save(*args, **kwargs)
      # Call the real save() method
    
    
    
class Conditions(models.Model):
    service=models.ForeignKey(Services, verbose_name='service_Conditions', on_delete=models.CASCADE)
    conditione=models.TextField(max_length=500)
    
    def __str__(self):
        return str(self.service)
    
       
class LastServices(models.Model):
    service=models.ForeignKey(Services, verbose_name='LastServices', on_delete=models.CASCADE)
    subtitle=models.TextField(max_length=300)
    description = models.TextField(max_length=5000)
    

class AboutUs(models.Model):
    description = models.TextField(max_length=5000)


class OurTeam(models.Model):
    pass

class Pricing(models.Model):
    pass

class Offers(models.Model):
    pass

class Review(models.Model):
    pass

class FaqAsked(models.Model):
    pass