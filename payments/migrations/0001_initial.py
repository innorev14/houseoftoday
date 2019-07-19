# Generated by Django 2.2.3 on 2019-07-17 05:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0006_auto_20190716_1209'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchant_uid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('imp_uid', models.CharField(blank=True, max_length=100)),
                ('name', models.CharField(max_length=100, verbose_name='상품명')),
                ('price', models.PositiveIntegerField(verbose_name='결제금액')),
                ('photo', models.ImageField(upload_to='')),
                ('status', models.CharField(choices=[('ready', '미결제'), ('paid', '결제완료'), ('cancelled', '결제취소'), ('failed', '결제실패')], db_index=True, default='ready', max_length=9)),
                ('meta', jsonfield.fields.JSONField(blank=True, default={})),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
