# Generated by Django 5.0.2 on 2024-02-24 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_category_slug_food_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='foo_name',
            new_name='category_name',
        ),
    ]