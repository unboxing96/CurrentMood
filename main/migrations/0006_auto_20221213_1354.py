# Generated by Django 3.2.13 on 2022-12-13 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_song_like_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='mqdefault_file',
            field=models.ImageField(default=3, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='song',
            name='default',
            field=models.URLField(default=None, max_length=130, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='hqdefault',
            field=models.URLField(default=None, max_length=130, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='mqdefault',
            field=models.URLField(default=None, max_length=130, null=True),
        ),
    ]
