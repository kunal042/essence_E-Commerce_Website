# Generated by Django 4.1.5 on 2023-02-15 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_checkout_checkoutproducts'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkoutproducts',
            name='pid',
            field=models.IntegerField(default=None),
        ),
    ]
