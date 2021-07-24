# Generated by Django 3.2.4 on 2021-07-22 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doska', '0008_ad_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story_title', models.CharField(blank=True, max_length=300, null=True, verbose_name='Заголовок')),
                ('story_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='images',
            name='ad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='doska.ad'),
        ),
        migrations.CreateModel(
            name='StoryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story_src', models.FileField(upload_to='stories/%Y/%m/%d/', verbose_name='Ресурс')),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doska.story')),
            ],
        ),
    ]
