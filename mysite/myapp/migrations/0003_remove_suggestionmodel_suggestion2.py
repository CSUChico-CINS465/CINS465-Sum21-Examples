# Generated by Django 3.2.4 on 2021-06-03 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_suggestionmodel_suggestion2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suggestionmodel',
            name='suggestion2',
        ),
    ]
