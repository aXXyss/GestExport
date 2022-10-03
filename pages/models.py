from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Page(models.Model):
    title = models.CharField(verbose_name="Titre", max_length=200)
    content = RichTextField(verbose_name="Contenu")
    order = models.SmallIntegerField(verbose_name="Ordre", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    updated = models.DateTimeField(auto_now=True, verbose_name='Date de modification')


    class Meta:
        verbose_name = 'page'
        verbose_name_plural = 'pages'
        ordering = ['order', 'title']

    def __str__(self):
        return self.title
