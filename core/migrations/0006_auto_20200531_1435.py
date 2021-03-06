# Generated by Django 2.2.4 on 2020-05-31 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_orderitem_item_variations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='billing_address',
        ),
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(choices=[('S', 'Shipping')], max_length=1),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('DO', 'DODO pizza'), ('BK', 'Burger King'), ('ZH', "Zheka's Doner House")], max_length=2),
        ),
    ]
