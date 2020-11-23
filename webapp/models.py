from django.db import models

# Create your models here.

class Tools(models.Model):
    """ Tools """
    name = models.CharField(max_length=100, primary_key=True, unique=True)
    acronym = models.CharField(max_length=100, blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    logo = models.CharField(max_length=200, blank=True, null=True)
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

class Social(models.Model):
    """ My social links """
    name = models.CharField(max_length=100, primary_key=True, unique=True)
    logo = models.CharField(max_length=200, blank=False, null=False)
    link = models.CharField(max_length=200, blank=False, null=False)
    order = models.IntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class Contact(models.Model):
    """ My contact intels """
    name = models.CharField(max_length=100, primary_key=True, unique=True)
    logo = models.CharField(max_length=200, blank=False, null=False)
    value = models.CharField(max_length=200, blank=False, null=False)
    link = models.CharField(max_length=200, blank=False, null=False)
    order = models.IntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name