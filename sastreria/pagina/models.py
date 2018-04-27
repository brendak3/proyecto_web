# sastreria
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    user_name = models.CharField(max_length = 30, blank = True)
    user_last = models.CharField(max_length = 30, blank = True)
    email = models.EmailField(blank = True)
    location = models.CharField(max_length = 30, blank = True)
    birth_date = models.DateField(null = True, blank = True)

    def __str__(self):
        return self.user.username

# Buscar en models las diferentes instancias
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)
    instance.perfil.save()

# Modelo de los productos del carrito de compras
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length = 100)
    precio = models.DecimalField(max_digits=6,decimal_places=2)
    image_url = models.CharField(max_length=100, blank=True)
    cantitad = models.IntegerField()

    def __str__(self):
        return self.nombre_producto
