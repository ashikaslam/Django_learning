# Generated by Django 5.0.1 on 2024-01-28 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='last_pub',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
