# Generated by Django 2.1.7 on 2020-01-24 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rootapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='setupcamera',
            name='camera_num',
            field=models.CharField(default='', max_length=50),
        ),
    ]