# Generated by Django 3.2.13 on 2022-11-30 01:24

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_user_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_img',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='user_img/'),
        ),
    ]