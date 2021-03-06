# Generated by Django 3.2.4 on 2021-06-11 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doska', '0002_auto_20210609_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Регион')),
                ('is_active', models.BooleanField(verbose_name='Активация')),
            ],
        ),
        migrations.AddField(
            model_name='ad',
            name='address',
            field=models.CharField(max_length=150, null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='ad',
            name='region',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='doska.region', verbose_name='Регион'),
        ),
    ]
