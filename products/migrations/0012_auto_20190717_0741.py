# Generated by Django 2.2.3 on 2019-07-17 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20190717_0740'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product_detail_images',
            new_name='ProductDetailImage',
        ),
    ]
