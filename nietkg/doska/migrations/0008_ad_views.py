# Generated by Django 3.2.4 on 2021-06-22 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doska', '0007_auto_20210621_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='views',
            field=models.PositiveIntegerField(default=0, verbose_name='Просмотры'),
        ),
    ]