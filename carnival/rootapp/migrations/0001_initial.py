# Generated by Django 2.1.7 on 2020-01-08 18:25

import carnival.rootapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_id', models.CharField(max_length=20)),
                ('date', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Setupcamera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dpt_id', models.CharField(max_length=10)),
                ('ip_address', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=100)),
                ('role', models.CharField(max_length=70)),
                ('dsgn', models.CharField(max_length=70)),
                ('img', models.ImageField(blank=True, null=True, upload_to=carnival.rootapp.models.rename_photo)),
            ],
        ),
    ]