# Generated by Django 3.2.5 on 2021-08-04 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffic', '0003_alter_light_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='light',
            name='state',
            field=models.CharField(choices=[('on', 'ON'), ('off', 'OFF')], max_length=3),
        ),
    ]
