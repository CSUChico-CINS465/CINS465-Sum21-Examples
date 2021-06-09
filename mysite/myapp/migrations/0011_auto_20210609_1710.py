# Generated by Django 3.2.4 on 2021-06-09 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20210609_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentmodel',
            name='image',
        ),
        migrations.RemoveField(
            model_name='commentmodel',
            name='image_description',
        ),
        migrations.AddField(
            model_name='suggestionmodel',
            name='image',
            field=models.ImageField(max_length=144, null=True, upload_to='uploads/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='suggestionmodel',
            name='image_description',
            field=models.CharField(max_length=240, null=True),
        ),
    ]
