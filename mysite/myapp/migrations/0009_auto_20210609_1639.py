# Generated by Django 3.2.4 on 2021-06-09 16:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_commentmodel_suggestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentmodel',
            name='published_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='suggestionmodel',
            name='published_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
