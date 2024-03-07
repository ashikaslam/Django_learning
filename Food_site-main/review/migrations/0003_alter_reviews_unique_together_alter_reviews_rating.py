# Generated by Django 5.0.2 on 2024-02-27 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_alter_reviews_rating'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reviews',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='rating',
            field=models.IntegerField(choices=[(1, '1 out of 5'), (2, '2 out of 5'), (3, '3 out of 5'), (4, '4 out of 5'), (5, '5 out of 5')]),
        ),
    ]
