# Generated by Django 3.2.13 on 2022-12-02 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_merge_0006_comment_0008_rename_likeitem_likesong'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='update_at',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(),
        ),
    ]