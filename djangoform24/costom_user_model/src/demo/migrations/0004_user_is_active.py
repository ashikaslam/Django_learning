# Generated by Django 5.0.4 on 2024-04-20 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_remove_user_is_active_user_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
    ]
