# Generated by Django 2.2.3 on 2019-07-15 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='detail_mfc',
            field=models.CharField(max_length=200),
        ),
    ]
