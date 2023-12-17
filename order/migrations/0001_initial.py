# Generated by Django 5.0 on 2023-12-16 02:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('establishment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=255, unique=True)),
                ('reserved_quantity', models.IntegerField()),
                ('amount_returned_by_customer', models.FloatField(max_length=255)),
                ('quantity_sold', models.CharField(max_length=255)),
                ('amount_charged', models.FloatField(max_length=255)),
                ('gift_or_discount', models.FloatField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('establishment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='establishment.establishment')),
            ],
        ),
    ]
