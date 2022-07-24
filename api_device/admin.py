from django.contrib import admin
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _

from .models  import Device, Meter, Customer, Node, AbstractUser
from .admin_export_csv import ExportCsv
import csv


@admin.register(AbstractUser)
class  AbstractUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'dev_eui', 'last_value', 'activated_time', 'on_or_off', 'description', 'device_type', 'owner')
    list_filter = ('dev_eui', 'owner', 'uuid')
    date_hierarchy = 'activated_time'
    actions = ['export_as_csv']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'email', 'description')
    list_filter = ('username', 'email')

@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'geo', 'name', 'description', 'address', 'owner')
    list_filter = ('uuid', 'name', 'description', 'address', 'owner')

@admin.register(Meter)
class MeterAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'uuid', 'on_or_off', 'registered_time', 'time_first_reading', 'beginning_value',
                    'unit')
    list_filter = ('serial_number', 'uuid')


