# Generated by Django 3.1.2 on 2020-11-23 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0025_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='img',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
