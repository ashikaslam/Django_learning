# Generated by Django 5.0.4 on 2024-05-19 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts_manager', '0006_alter_instructorsprofile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationsforinstructors',
            name='gender',
            field=models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], max_length=10),
        ),
    ]
