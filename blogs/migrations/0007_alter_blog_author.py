# Generated by Django 3.2.4 on 2021-07-21 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_auto_20210721_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(null=True, on_delete=models.SET('Anonymous'), related_name='blogs', to='blogs.author'),
        ),
    ]