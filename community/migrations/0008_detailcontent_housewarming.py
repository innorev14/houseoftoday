# Generated by Django 2.2.3 on 2019-07-31 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0007_detailcontent_housewarming_housewarmingcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailcontent',
            name='housewarming',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='detail_contents', to='community.Housewarming'),
        ),
    ]