# Generated by Django 4.0.5 on 2022-06-20 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_content', '0002_remove_postlovereact_liked_postsmodel_topic_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcastmodel',
            name='audio_file',
            field=models.FileField(upload_to='music/'),
        ),
    ]
