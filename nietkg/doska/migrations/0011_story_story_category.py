# Generated by Django 3.2.4 on 2021-07-23 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doska', '0010_storyitem_story_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='story_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='doska.category'),
        ),
    ]
