# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cartridge.shop.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20150811_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='key',
            field=models.CharField(max_length=40, db_index=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=cartridge.shop.fields.SKUField(null=True, max_length=20, verbose_name='SKU', blank=True),
        ),
        migrations.AlterField(
            model_name='productvariation',
            name='sku',
            field=cartridge.shop.fields.SKUField(null=True, max_length=20, verbose_name='SKU', blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together=set([('sku', 'site')]),
        ),
    ]
