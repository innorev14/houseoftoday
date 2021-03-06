# Generated by Django 2.2.3 on 2019-07-23 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20190723_0344'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotDealNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_rnd_number', models.PositiveIntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
