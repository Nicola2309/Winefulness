# Generated by Django 3.2 on 2021-05-28 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winemakers', '0004_auto_20210527_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='winemakers',
            name='location',
            field=models.CharField(max_length=120),
        ),
    ]
