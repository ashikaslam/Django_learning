# Generated by Django 5.0.2 on 2024-02-23 15:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cartitem_user_alter_cartitem_cart'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product'),
        ),
    ]