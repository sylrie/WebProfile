# Generated by Django 3.1.2 on 2020-10-19 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20201017_1334'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='devtool',
            options={'ordering': ['-family', '-tool_type']},
        ),
        migrations.AddField(
            model_name='toolfamily',
            name='info',
            field=models.TextField(blank=True),
        ),
    ]
