# Generated by Django 2.2.5 on 2019-10-09 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bms', '0002_remove_brand_brand_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='brand_code',
            field=models.IntegerField(default=1, unique=True, verbose_name='Brand Code'),
            preserve_default=False,
        ),
    ]