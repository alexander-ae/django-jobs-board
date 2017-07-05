from django.db import models
from django.utils.translation import ugettext as _
from . import constants


class Company(models.Model):
    name = models.CharField(max_length=75)
    url = models.URLField(verbose_name=_('URL'), blank=True)
    location = models.CharField(max_length=120, blank=True)
    coordinates = models.CharField(max_length=64, help_text='lat,lon', blank=True)
    summary = models.CharField(max_length=128)
    size = models.CharField(_('Company size'), max_length=64, choices=constants.COMPANY_SIZE)
    employees = models.CharField(_('Quantity of employees'), max_length=64, choices=constants.COMPANY_EMPLOYEES)

    # contact
    contact_name = models.CharField(_('Contact name'), max_length=128)
    contact_email = models.CharField(_('Contact email'), max_length=128)
    contact_phone = models.CharField(_('Contact phone'), max_length=128)
    contact_position = models.CharField(_('Contact position'), max_length=128)

    class Meta:
        verbose_name_plural = 'Companies'
        ordering = ['name']

    def __str__(self):
        return self.name
