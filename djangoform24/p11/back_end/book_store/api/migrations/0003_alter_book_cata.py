# Generated by Django 5.0.1 on 2024-02-05 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_book_cata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cata',
            field=models.CharField(choices=[('f', 'funny'), ('h', 'horor'), ('s', 'sifi'), ('j', 'jock'), ('Mystery', 'Mystery'), ('Thriller', 'Thriller'), ('Humor', 'Humor'), ('Horror', 'Horror'), ('Sci-Fi', 'Sci-Fi')], max_length=30, null=True),
        ),
    ]
