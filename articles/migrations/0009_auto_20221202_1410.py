# Generated by Django 3.2.13 on 2022-12-02 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_rename_likeitem_likesong'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likesong',
            name='article',
        ),
        migrations.RemoveField(
            model_name='likesong',
            name='like',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
        migrations.DeleteModel(
            name='Likesong',
        ),
    ]