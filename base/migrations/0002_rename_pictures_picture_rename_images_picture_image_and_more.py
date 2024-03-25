# Generated by Django 4.1.4 on 2024-03-15 11:28

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='pictures',
            new_name='Picture',
        ),
        migrations.RenameField(
            model_name='picture',
            old_name='images',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='picture',
            old_name='upload_data',
            new_name='upload_date',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='upload_data',
            new_name='upload_date',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='uploader',
            new_name='user',
        ),
    ]