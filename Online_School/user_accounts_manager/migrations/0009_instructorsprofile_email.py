# Generated by Django 5.0.4 on 2024-05-19 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts_manager', '0008_alter_instructorsprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructorsprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]