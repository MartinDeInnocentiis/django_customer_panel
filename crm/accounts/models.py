from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class Profile (models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField (max_length=200,null=True, blank=True)
    last_name = models.CharField (max_length=200,null=True, blank=True)
    phone = models.CharField (max_length=200,null=True, blank=True)
    
    
    def __str__(self) -> str:
        return str(self.user)
    
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print ('Created profile')
post_save.connect(create_profile, sender=User)

    
def update_profile(sender, instance, created, **kwargs):

    if created == False:
        instance.profile.save()
        print('Profile updated')
post_save.connect(create_profile, sender=User)


class Customer (models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField (max_length=200,null=True)
    phone = models.CharField (max_length=200,null=True)
    email = models.EmailField (max_length=200,null=True)
    profile_pic = models.ImageField (default= 'avatar1.png', null=True, blank=True)
    date_created = models.DateField (auto_now_add=True,null=True)
    
    def __str__(self):
        return self.name
    
class Tag (models.Model):
    name = models.CharField (max_length=200,null=True)
    
    def __str__(self):
        return self.name   
       

    
class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door'),
    )
    name = models.CharField (max_length=200,null=True)
    price = models.FloatField(null=True)
    category = models.CharField (max_length=200,null=True, choices = CATEGORY)
    description = models.CharField (max_length=200,null=True, blank=True)
    date_created = models.DateField (auto_now_add=True,null=True)
    tags = models.ManyToManyField(Tag)
        
    def __str__(self):
        return self.name   
    
class Order (models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out of delivery', 'Out of delivery'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product =  models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateField (auto_now_add=True,null=True)
    status = models.CharField (max_length=200,null=True, choices=STATUS) #CADA VEZ QUE CREO UNA ORDEN TIENE UN MENÚ DESPLEGABLE CON LAS OPCIONES STATUS
    note = models.CharField (max_length=200,null=True)

    def __str__(self):
        return self.product.name   