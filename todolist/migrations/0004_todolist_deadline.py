# Generated by Django 4.1 on 2022-10-16 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_todolist_is_finished'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='deadline',
            field=models.TextField(default='16-02-2002'),
        ),
    ]
