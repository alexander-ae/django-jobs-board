from django.contrib.postgres.fields import IntegerRangeField
from django.db import models
from django.utils.translation import ugettext as _
from companies.models import Company
from core.models import SlugModel


class Category(SlugModel):
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ('name',)


class Job(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=64)
    description = models.TextField()

    category = models.ForeignKey(Category)

    company = models.ForeignKey(Company)
    location = models.CharField(max_length=120, blank=True)
    coordinates = models.CharField(max_length=64, help_text='lat,lon', blank=True)

    salary = IntegerRangeField()
    email = models.EmailField()

    class Meta:
        verbose_name = _('Job')
        verbose_name_plural = _('Jobs')
        ordering = ('-created_at',)

    def __str__(self):
        return self.title
