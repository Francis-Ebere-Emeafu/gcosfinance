# Generated by Django 3.1.1 on 2021-06-28 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='author',
        ),
    ]
