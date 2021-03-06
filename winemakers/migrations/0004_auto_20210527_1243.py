# Generated by Django 3.2 on 2021-05-27 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winemakers', '0003_rename_title_winemakers_producer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='winemakers',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='winemakers',
            name='image_url',
            field=models.URLField(blank=True, default='', max_length=1024),
        ),
    ]
