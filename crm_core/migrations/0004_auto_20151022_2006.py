
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('crm_core', '0003_auto_20150905_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companycontactdata',
            name='logo',
            field=models.ImageField(verbose_name='Logo', null=True, upload_to='', blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='contract',
            name='dateofcreation',
            field=django_extensions.db.fields.CreationDateTimeField(verbose_name='Created at', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='lastmodification',
            field=django_extensions.db.fields.ModificationDateTimeField(verbose_name='Last modified', auto_now=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='dateofcreation',
            field=django_extensions.db.fields.CreationDateTimeField(verbose_name='Created at', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='lastmodification',
            field=django_extensions.db.fields.ModificationDateTimeField(verbose_name='Last modified', auto_now=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='prefix',
            field=models.CharField(verbose_name='Title', choices=[('F', 'Company'), ('H', 'Mr'), ('W', 'Mrs'), ('G', 'Ms')], null=True, blank=True, max_length=1),
        ),
        migrations.AlterField(
            model_name='customeremailaddress',
            name='purpose',
            field=models.CharField(verbose_name='Purpose', choices=[('H', 'Private'), ('O', 'Business')], default='H', max_length=1),
        ),
        migrations.AlterField(
            model_name='customerphoneaddress',
            name='purpose',
            field=models.CharField(verbose_name='Purpose', choices=[('H', 'Private'), ('O', 'Business'), ('P', 'Mobile Private'), ('B', 'Mobile Business')], default='H', max_length=1),
        ),
        migrations.AlterField(
            model_name='customerpostaladdress',
            name='purpose',
            field=models.CharField(verbose_name='Purpose', choices=[('D', 'Delivery Address'), ('B', 'Billing Address'), ('C', 'Contact Address')], default='C', max_length=1),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='dateofcreation',
            field=django_extensions.db.fields.CreationDateTimeField(verbose_name='Created at', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='lastmodification',
            field=django_extensions.db.fields.ModificationDateTimeField(verbose_name='Last modified', auto_now=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='dateofcreation',
            field=django_extensions.db.fields.CreationDateTimeField(verbose_name='Created at', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='lastmodification',
            field=django_extensions.db.fields.ModificationDateTimeField(verbose_name='Last modified', auto_now=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='dateofcreation',
            field=django_extensions.db.fields.CreationDateTimeField(verbose_name='Created at', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='lastmodification',
            field=django_extensions.db.fields.ModificationDateTimeField(verbose_name='Last modified', auto_now=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='dateofcreation',
            field=django_extensions.db.fields.CreationDateTimeField(verbose_name='Created at', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='lastmodification',
            field=django_extensions.db.fields.ModificationDateTimeField(verbose_name='Last modified', auto_now=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='prefix',
            field=models.CharField(verbose_name='Title', choices=[('F', 'Company'), ('H', 'Mr'), ('W', 'Mrs'), ('G', 'Ms')], null=True, blank=True, max_length=1),
        ),
        migrations.AlterField(
            model_name='supplieremailaddress',
            name='purpose',
            field=models.CharField(verbose_name='Purpose', choices=[('H', 'Private'), ('O', 'Business')], default='H', max_length=1),
        ),
        migrations.AlterField(
            model_name='supplierphoneaddress',
            name='purpose',
            field=models.CharField(verbose_name='Purpose', choices=[('H', 'Private'), ('O', 'Business'), ('P', 'Mobile Private'), ('B', 'Mobile Business')], default='H', max_length=1),
        ),
        migrations.AlterField(
            model_name='supplierpostaladdress',
            name='purpose',
            field=models.CharField(verbose_name='Purpose', choices=[('D', 'Delivery Address'), ('B', 'Billing Address'), ('C', 'Contact Address')], default='C', max_length=1),
        ),
        migrations.AlterField(
            model_name='userextension',
            name='image',
            field=models.ImageField(verbose_name='Bild', null=True, blank=True, default='avatars/avatar.jpg', upload_to='avatars/'),
        ),
    ]
