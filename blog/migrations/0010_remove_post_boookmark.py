# Generated by Django 2.2.4 on 2020-03-19 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200319_1614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='boookmark',
        ),
    ]
