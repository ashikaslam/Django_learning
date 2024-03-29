# Generated by Django 5.0.1 on 2024-02-05 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('cata', models.CharField(choices=[('f', 'funny'), ('h', 'horor'), ('s', 'sifi'), ('j', 'jock')], max_length=30)),
                ('author', models.CharField(max_length=20)),
                ('first_pub', models.DateTimeField(auto_now_add=True)),
                ('last_pub', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
