from django.db import models

# Create your models here.

class Link(models.Model):
    key = models.SlugField(verbose_name="Clé", max_length=100, unique=True)
    name = models.CharField(verbose_name="Réseau social", max_length=200)
    url = models.URLField(verbose_name="Lien", max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    updated = models.DateTimeField(auto_now=True, verbose_name='Date de modification')


    class Meta:
        verbose_name = 'lien'
        verbose_name_plural = 'liens'
        ordering = ['name']

    def __str__(self):
        return self.name