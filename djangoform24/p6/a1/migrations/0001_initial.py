# Generated by Django 5.0.1 on 2024-01-25 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('roll', models.IntegerField(primary_key=True, serialize=False)),
                ('addrress', models.TextField()),
            ],
        ),
    ]
