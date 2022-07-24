import uuid as uuid

from django.db import models

class AbstractUser(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='First name')
    last_name = models.CharField(max_length=100, verbose_name='Last name')


    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

class Device(models.Model):
    ON_OR_OFF = [
        ('On', 'On'),
        ('Off', 'Off')
    ]
    uuid = models.UUIDField(verbose_name='UUID', default=uuid.uuid4())
    dev_eui = models.CharField(max_length=20, verbose_name='Device\'s ID')
    last_value = models.DateTimeField(verbose_name='Time of last reading')
    activated_time = models.DateTimeField(verbose_name='Activation time', auto_now_add=True)
    on_or_off = models.CharField(max_length=100, verbose_name='Device on or off', choices=ON_OR_OFF)
    description = models.CharField(max_length=250, verbose_name="Description")
    device_type = models.CharField(max_length=100, verbose_name='Device type')
    owner = models.ForeignKey(AbstractUser, verbose_name='Owner', on_delete=models.CASCADE)

class Meter(models.Model):
    ON_OR_OFF = [
        ('On', 'On'),
        ('Off', 'Off')
    ]
    serial_number = models.IntegerField(verbose_name='Serial Number')
    uuid = models.UUIDField(verbose_name='UUID', default=uuid.uuid4())
    on_or_off = models.CharField(max_length=100, verbose_name='Device on or off', choices=ON_OR_OFF)
    registered_time = models.DateTimeField(verbose_name='Registered time', auto_now_add=True)
    time_first_reading = models.DateTimeField(verbose_name='Time of first readinf', auto_now_add=True)
    beginning_value = models.IntegerField(verbose_name="Beginning value in meter")
    unit = models.CharField(max_length=50, verbose_name='Unit of meter')
    owner = models.ForeignKey(AbstractUser, verbose_name='Owner', on_delete=models.CASCADE)

class Node(models.Model):
    uuid = models.UUIDField(verbose_name='UUID', default=uuid.uuid4())
    geo = models.DecimalField(verbose_name='Geo data', max_digits=10, decimal_places=10)
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.CharField(max_length=100, verbose_name='Description', blank=True)
    owner = models.ForeignKey(AbstractUser, verbose_name='Owner', blank=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, verbose_name='Address')

class Customer(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='First name')
    last_name = models.CharField(max_length=100, verbose_name='Last name')
    username = models.CharField(max_length=100, verbose_name='Username')
    email = models.EmailField(max_length=100, verbose_name='Email address')
    description = models.CharField(max_length=100, verbose_name='Description')



