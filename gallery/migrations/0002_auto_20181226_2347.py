# Generated by Django 2.1.3 on 2018-12-26 18:17

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=stdimage.models.StdImageField(blank=True, upload_to='images/'),
        ),
    ]
