# Generated by Django 4.2.6 on 2023-10-21 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_alter_chatroom_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
