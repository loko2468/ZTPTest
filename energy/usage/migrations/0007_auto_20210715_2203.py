# Generated by Django 2.2 on 2021-07-15 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usage', '0006_auto_20210715_2050'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='file',
            options={},
        ),
        migrations.RemoveField(
            model_name='file',
            name='title',
        ),
    ]
