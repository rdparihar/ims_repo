# Generated by Django 2.2.5 on 2019-10-11 12:07

from decimal import Decimal
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
            name='BmsUser',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='User Id')),
                ('user_first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('user_last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('user_role', models.CharField(choices=[('A', 'ADMIN'), ('S', 'SUBADMIN'), ('U', 'USER')], default='U', max_length=1, verbose_name='User Role')),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Bms User',
                'verbose_name_plural': 'Bms User',
                'ordering': ['-user_id'],
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('brand_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Brand Id')),
                ('brand_code', models.IntegerField(unique=True, verbose_name='Brand Code')),
                ('brand_name', models.CharField(max_length=200, verbose_name='Brand Name')),
                ('brand_p_cost', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=22)),
                ('brand_q_cost', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=22)),
                ('brand_n_cost', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=22)),
                ('brand_d_cost', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=22)),
                ('brand_l_cost', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=22)),
                ('brand_xg_cost', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=22)),
                ('brand_y_cost', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=22)),
                ('brand_p_sale', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=22)),
                ('brand_q_sale', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=22)),
                ('brand_n_sale', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=22)),
                ('brand_d_sale', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=22)),
                ('brand_l_sale', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=22)),
                ('brand_xg_sale', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=22)),
                ('brand_y_sale', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=22)),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
                'ordering': ['brand_id'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Category Id')),
                ('category_name', models.CharField(max_length=200, verbose_name='Category Name')),
                ('category_description', models.CharField(max_length=200, verbose_name='Category Description')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Category',
                'ordering': ['category_id'],
                'permissions': (('can_see_category', 'Can see category'),),
            },
        ),
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('quantity_name', models.CharField(max_length=4, primary_key=True, serialize=False, verbose_name='Quantity Name')),
                ('quantity_bottles', models.IntegerField(verbose_name='Quantity bottles')),
            ],
            options={
                'verbose_name': 'Quantity',
                'verbose_name_plural': 'Quantities',
                'ordering': ['quantity_name'],
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('shop_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Shop Id')),
                ('shop_name', models.CharField(max_length=200, verbose_name='Shop Name')),
                ('shop_address', models.CharField(max_length=200, verbose_name='Shop Address')),
                ('shop_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bms.BmsUser')),
                ('shop_keeper', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='bms.BmsUser')),
            ],
            options={
                'verbose_name': 'Shop',
                'verbose_name_plural': 'Shop',
                'ordering': ['shop_id'],
            },
        ),
        migrations.CreateModel(
            name='StockOpen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_date', models.DateField(verbose_name='Stock Open Date')),
                ('open_p', models.IntegerField(verbose_name='Stock Open P')),
                ('open_q', models.IntegerField(verbose_name='Stock Open Q')),
                ('open_n', models.IntegerField(verbose_name='Stock Open N')),
                ('open_d', models.IntegerField(verbose_name='Stock Open D')),
                ('open_l', models.IntegerField(verbose_name='Stock Open L')),
                ('open_xg', models.IntegerField(verbose_name='Stock Open XG')),
                ('open_y', models.IntegerField(verbose_name='Stock Open Y')),
                ('brand_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bms.Brand')),
                ('open_shop_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bms.Shop', verbose_name='Stock Open Shop')),
            ],
            options={
                'verbose_name': 'StockOpen',
                'verbose_name_plural': 'StockOpens',
                'ordering': ['open_date'],
            },
        ),
        migrations.CreateModel(
            name='StockClose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('close_date', models.DateField(verbose_name='Stock Close Date')),
                ('close_qty_p', models.IntegerField(verbose_name='Stock Close Qty P')),
                ('close_qty_q', models.IntegerField(verbose_name='Stock Close Qty Q')),
                ('close_qty_n', models.IntegerField(verbose_name='Stock Close Qty N')),
                ('close_qty_d', models.IntegerField(verbose_name='Stock Close Qty D')),
                ('close_qty_l', models.IntegerField(verbose_name='Stock Close Qty L')),
                ('close_qty_xg', models.IntegerField(verbose_name='Stock Close Qty XG')),
                ('close_qty_y', models.IntegerField(verbose_name='Stock Close Qty Y')),
                ('close_sale_p', models.IntegerField(verbose_name='Stock Close Sale P')),
                ('close_sale_q', models.IntegerField(verbose_name='Stock Close Sale Q')),
                ('close_sale_n', models.IntegerField(verbose_name='Stock Close Sale N')),
                ('close_sale_d', models.IntegerField(verbose_name='Stock Close Sale D')),
                ('close_sale_l', models.IntegerField(verbose_name='Stock Close Sale L')),
                ('close_sale_xg', models.IntegerField(verbose_name='Stock Close Sale XG')),
                ('close_sale_y', models.IntegerField(verbose_name='Stock Close Sale Y')),
                ('total_sale', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=22)),
                ('brand_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bms.Brand')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bms.Category', verbose_name='Stock Category')),
                ('close_shop_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bms.Shop', verbose_name='Stock Close Shop')),
            ],
            options={
                'verbose_name': 'StockClose',
                'verbose_name_plural': 'StockCloses',
                'ordering': ['close_date'],
            },
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_shift_date', models.DateField(verbose_name='Stock Shift Date')),
                ('stock_shift_from', models.IntegerField(verbose_name='Stock Shift From Shop')),
                ('stock_shift_p', models.IntegerField(verbose_name='Stock Shift P')),
                ('stock_shift_q', models.IntegerField(verbose_name='Stock Shift Q')),
                ('stock_shift_n', models.IntegerField(verbose_name='Stock Shift N')),
                ('stock_shift_d', models.IntegerField(verbose_name='Stock Shift D')),
                ('stock_shift_l', models.IntegerField(verbose_name='Stock Shift L')),
                ('stock_shift_xg', models.IntegerField(verbose_name='Stock Shift XG')),
                ('stock_shift_y', models.IntegerField(verbose_name='Stock Shift Y')),
                ('brand_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bms.Brand')),
                ('stock_shift_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bms.Shop', verbose_name='Stock Shift To Shop')),
            ],
            options={
                'verbose_name': 'Shift',
                'verbose_name_plural': 'Shifts',
                'ordering': ['stock_shift_date'],
            },
        ),
        migrations.AddField(
            model_name='brand',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bms.Category'),
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoice_transaction_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Invoice Id')),
                ('invoice_date', models.DateField(verbose_name='Invoice Date')),
                ('invoice_brand_size', models.CharField(max_length=5, verbose_name='Brand Size')),
                ('invoice_brand_qty', models.IntegerField(verbose_name='Brand Quantity')),
                ('invoice_rate_per_case', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=22)),
                ('invoice_no_of_cases', models.IntegerField(verbose_name='Number of Cases')),
                ('invoice_total', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=22)),
                ('brand_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bms.Brand')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bms.Category')),
                ('shop_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bms.Shop')),
            ],
            options={
                'verbose_name': 'invoice',
                'verbose_name_plural': 'invoice',
                'ordering': ['invoice_transaction_id'],
                'unique_together': {('brand_id', 'shop_id', 'invoice_brand_size', 'invoice_date')},
            },
        ),
    ]
