# Generated by Django 4.0.3 on 2022-03-15 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='datetime_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
