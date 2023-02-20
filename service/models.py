from django.db import models
from django.utils.text import slugify

# Create your models here.
class Service(models.Model):
    name=models.CharField( max_length=50)
    title= models.CharField(max_length=200)
    subtitle=models.TextField(max_length=500)
    description=models.TextField(max_length=10000)
    ser_image=models.ImageField(upload_to='Service')
    det_image=models.ImageField( upload_to='Service',blank=True,null=True)
    slug=models.SlugField(null=True,blank=True)
    
    def __str__(self) :
        return str(self.name)
    
    def save(self, *args, **kwargs):
       self.slug=slugify(self.name)
       super(Service, self).save(*args, **kwargs)
      # Call the real save() method
    
    
    
class Condition(models.Model):
    service=models.ForeignKey(Service, related_name='service_Condition', on_delete=models.CASCADE)
    conditione=models.TextField(max_length=500)
    
    def __str__(self):
        return str(self.service)
    
       
class LastService(models.Model):
    service=models.ForeignKey(Service, related_name='Last_Service', on_delete=models.CASCADE)
    subtitle=models.TextField(max_length=300)
    description = models.TextField(max_length=5000)
    
    def __str__(self):
        return str(self.service)

class About(models.Model):
    about_us = models.TextField(max_length=5000)
    image=models.ImageField( upload_to='about_us')

    def __str__(self):
        return str(self.about_us)
    

class OurTeam(models.Model):
    name = models.CharField(max_length = 50)
    job=models.CharField(max_length = 50)
    image=models.ImageField( upload_to='OurTeam')
    job_info = models.TextField(max_length=300)
    facebook=models.CharField(max_length = 150)
    instagram=models.CharField(max_length = 150)
    linkedin=models.CharField(max_length = 150)
    
    def __str__(self):
        return str(self.name)

class Pricing(models.Model):
    plane_name=models.CharField(max_length = 200)
    price=models.DecimalField( max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.plane_name)
    
    
class Offer(models.Model):
    plane_name=models.ForeignKey(Pricing, related_name='Pricing_Offer', on_delete=models.CASCADE)
    offers=models.CharField(max_length = 200)
    
    def __str__(self):
        return str(self.plane_name)
    
    
class Review(models.Model):
    service=models.ForeignKey(Service, related_name='Service_Review', on_delete=models.CASCADE)
    rate=models.IntegerField()
    review = models.TextField(max_length=1000)
    
    def __str__(self):
        return str(self.service)
    

class FaqAsked(models.Model):
    ask = models.CharField(max_length = 200)
    answer = models.TextField(1000)
    
    def __str__(self):
        return str(self.ask)
    
    