# Generated by Django 2.2.4 on 2021-01-24 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_todomodel_is_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
    ]
