# Generated by Django 2.2.5 on 2019-10-10 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bms', '0004_auto_20191009_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand_code',
            field=models.IntegerField(unique=True, verbose_name='Brand Code'),
        ),
        migrations.AlterUniqueTogether(
            name='invoice',
            unique_together={('brand_id', 'invoice_brand_size', 'invoice_date')},
        ),
    ]