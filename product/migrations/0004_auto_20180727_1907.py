# Generated by Django 2.0.7 on 2018-07-27 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-timestamp', '-last_updated']},
        ),
        migrations.AddField(
            model_name='product',
            name='last_updated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='timestamp',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
