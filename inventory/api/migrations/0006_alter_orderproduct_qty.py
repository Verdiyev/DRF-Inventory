# Generated by Django 4.0.3 on 2022-03-24 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_order_status_orderproduct_qty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='qty',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
