# Generated by Django 3.2.4 on 2021-07-21 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_auto_20210721_1649'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='first_name',
            new_name='user_name',
        ),
        migrations.RemoveField(
            model_name='author',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='blog',
            name='excerpt',
            field=models.CharField(max_length=100),
        ),
    ]
