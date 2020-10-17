from django.db import models

# Create your models here.

class ToolFamily(models.Model):
    """ Tool Families """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class ToolType(models.Model):
    """ Tool Types """
    name = models.CharField(max_length=100, unique=True)
    info = models.TextField(blank=True)

    def __str__(self):
        return self.name


class DevTool(models.Model):
    """ Tools """
    family = models.ForeignKey(ToolFamily, on_delete=models.CASCADE)
    tool_type = models.ForeignKey(ToolType, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=False, unique=True)
    acronym = models.CharField(max_length=100, blank=True, null=True, unique=True)
    info = models.TextField(null=False)
    info_source = models.CharField(max_length=100, blank=True, null=True)
    source_name = models.CharField(max_length=100, blank=True, null=True)
    img = models.CharField(max_length=50, blank=True, null=True)
    logo = models.CharField(max_length=50, blank=True, null=True)
    
    class Meta:
        ordering = ['family']

    def __str__(self):
        return self.name