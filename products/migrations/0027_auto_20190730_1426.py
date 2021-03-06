# Generated by Django 2.2.3 on 2019-07-30 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0026_auto_20190726_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_product', to='products.Payment'),
        ),
        migrations.CreateModel(
            name='DirectPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_price', models.PositiveIntegerField(default=0)),
                ('deliver_price', models.PositiveIntegerField(default=0)),
                ('total_price', models.PositiveIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('product_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='directorder', to='products.ProductOption')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='directorder', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='direct_payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_product', to='products.DirectPayment'),
        ),
    ]
