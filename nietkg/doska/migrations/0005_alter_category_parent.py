# Generated by Django 3.2.4 on 2021-06-13 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doska', '0004_alter_region_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='doska.category'),
        ),
    ]