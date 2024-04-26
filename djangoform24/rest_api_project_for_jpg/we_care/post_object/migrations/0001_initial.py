# Generated by Django 5.0.4 on 2024-04-24 12:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('impage1', models.ImageField(blank=True, upload_to='photos/post')),
                ('impage2', models.ImageField(blank=True, upload_to='photos/post')),
                ('blood_grpup', models.CharField(choices=[('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('O+', 'O+'), ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'AB-'), ('O-', 'O-')], max_length=3)),
                ('amount', models.DecimalField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)], decimal_places=1, default=0.0, max_digits=3)),
                ('post_time', models.DateTimeField(auto_now_add=True)),
                ('post_update_time', models.DateTimeField(auto_now=True)),
                ('blood_need_time', models.DateTimeField()),
                ('apply_availavle', models.BooleanField(default=True)),
                ('people_apply', models.IntegerField()),
                ('at_leas_5_people_managed', models.IntegerField()),
                ('donate_done', models.BooleanField(default=False)),
                ('country', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('upazila', models.CharField(max_length=50)),
                ('unionOrtown', models.CharField(max_length=50)),
                ('villageOrrad', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=5)),
                ('hospital_name', models.CharField(max_length=50)),
                ('helper', models.ManyToManyField(blank=True, related_name='i_helped', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_post', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]