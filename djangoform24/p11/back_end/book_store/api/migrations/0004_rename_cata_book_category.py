# Generated by Django 5.0.1 on 2024-02-05 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_book_cata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='cata',
            new_name='category',
        ),
    ]
