# Generated by Django 3.1.2 on 2020-11-20 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_auto_20201120_1657'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tools',
            options={'ordering': ['order'], 'verbose_name_plural': 'Outils'},
        ),
        migrations.AddField(
            model_name='tools',
            name='order',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
