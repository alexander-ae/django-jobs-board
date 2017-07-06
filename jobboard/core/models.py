from django.db import models
from django.utils.translation import ugettext as _
from uuslug import uuslug


class SlugModel(models.Model):
    ''' Modelo abstracto utilizado para manejar el campo slug '''

    name = models.CharField(_('Name'), max_length=120)
    slug = models.SlugField(_('Slug'), max_length=180, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.name, instance=self)
        super(SlugModel, self).save(*args, **kwargs)

