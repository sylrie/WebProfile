# Generated by Django 3.1.2 on 2020-10-15 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20201015_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='devtool',
            name='source_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]