# Generated by Django 2.2.3 on 2019-07-22 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20190718_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount_rate',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]