# Generated by Django 3.2.5 on 2021-07-31 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffic', '0002_light_road'),
    ]

    operations = [
        migrations.AlterField(
            model_name='light',
            name='name',
            field=models.CharField(choices=[('light1', 'light1'), ('light2', 'light2'), ('light3', 'light3'), ('light4', 'light4'), ('light5', 'light5'), ('light6', 'light6'), ('light7', 'light7')], help_text='The light on the road', max_length=20),
        ),
    ]
