# Generated by Django 2.2.4 on 2019-10-23 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191023_2249'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_date',
            new_name='create_date',
        ),
    ]
