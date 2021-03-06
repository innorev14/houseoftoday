# Generated by Django 2.2.3 on 2019-07-12 02:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('price', models.IntegerField()),
                ('brand_name', models.CharField(max_length=45)),
                ('detail_name', models.CharField(max_length=100)),
                ('detail_color', models.CharField(max_length=30)),
                ('detail_size', models.CharField(max_length=100)),
                ('detail_component', models.CharField(max_length=45)),
                ('detail_auth', models.CharField(max_length=45)),
                ('detail_cost', models.CharField(max_length=45)),
                ('detail_standard', models.CharField(max_length=100)),
                ('detail_mfc', models.CharField(max_length=50)),
                ('detail_mis', models.CharField(max_length=45)),
                ('detail_as', models.CharField(max_length=100)),
                ('return_fee', models.CharField(max_length=100)),
                ('exchange_fee', models.CharField(max_length=100)),
                ('return_address', models.TextField()),
                ('deliver', models.CharField(default='업체직접배송', max_length=100)),
                ('deliver_fee', models.CharField(default='무료배송', max_length=100)),
                ('deliver_no_go', models.CharField(default='배송불가지역이 없습니다.', max_length=100)),
                ('deliver_fee_diff', models.CharField(default='없음', max_length=100)),
                ('created', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='products.Categorys')),
            ],
        ),
        migrations.CreateModel(
            name='reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pd_durability', models.IntegerField()),
                ('pd_price', models.IntegerField()),
                ('pd_design', models.IntegerField()),
                ('pd_delivery', models.IntegerField()),
                ('rv_image', models.ImageField(upload_to='')),
                ('comment', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
                ('helpful', models.ManyToManyField(blank=True, related_name='helpful_reviews', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='products.Products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product_thumnail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pd_image', models.ImageField(upload_to='')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_thumnail', to='products.Products')),
            ],
        ),
        migrations.CreateModel(
            name='Product_options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=45)),
                ('option_name', models.CharField(max_length=100)),
                ('option_price', models.PositiveIntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_options', to='products.Products')),
            ],
        ),
        migrations.CreateModel(
            name='Product_detail_images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pd_detail_image', models.ImageField(upload_to='')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_detail_images', to='products.Products')),
            ],
        ),
        migrations.CreateModel(
            name='PD_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
                ('comment', models.TextField()),
                ('completed', models.BooleanField(default=False)),
                ('created', models.DateField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='products.Products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PD_Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='products.PD_Question')),
            ],
        ),
    ]
