# Generated by Django 2.0.7 on 2018-08-01 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20180801_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='slug1',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]