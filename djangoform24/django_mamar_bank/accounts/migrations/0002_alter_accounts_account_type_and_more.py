# Generated by Django 5.0.1 on 2024-02-10 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='account_type',
            field=models.CharField(choices=[('SAVING', 'SAVING'), ('CURRENT', 'CURRENT')], max_length=10),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
