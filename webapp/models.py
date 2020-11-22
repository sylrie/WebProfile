from django.db import models

# Create your models here.

class Tools(models.Model):
    """ Tools """
    name = models.CharField(max_length=100, primary_key=True, unique=True)
    acronym = models.CharField(max_length=200, blank=True, null=True)
    infos = models.TextField(blank=True, null=True)
    logo = models.CharField(max_length=100, blank=True, null=True)
    order = models.IntegerField()

    class Meta:
        verbose_name_plural = "Outils"
        ordering = ['order']

    def __str__(self):
        return self.name

class Steps(models.Model):
    """ Tools """
    name = models.CharField(max_length=100, primary_key=True, unique=True)
    infos = models.TextField(blank=True, null=True)
    logo = models.CharField(max_length=200, blank=True, null=True)
    order = models.IntegerField()

    class Meta:
        verbose_name_plural = "Etapes"
        ordering = ['order']

    def __str__(self):
        return self.name

