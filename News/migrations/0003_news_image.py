# Generated by Django 3.1.6 on 2021-11-12 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0002_auto_20211112_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(default='', upload_to='news/images'),
        ),
    ]
