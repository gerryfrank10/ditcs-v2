# Generated by Django 3.2.5 on 2021-07-24 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traffic', '0003_auto_20210724_1300'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Exchange',
            new_name='Junction',
        ),
        migrations.RenameField(
            model_name='road',
            old_name='exchange',
            new_name='junction',
        ),
    ]