# Generated by Django 3.2.5 on 2021-07-25 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffic', '0004_auto_20210724_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='road',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='traffic',
            name='time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]