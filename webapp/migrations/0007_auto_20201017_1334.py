# Generated by Django 3.1.2 on 2020-10-17 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_tooltype_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='devtool',
            name='img',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='devtool',
            name='logo',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
