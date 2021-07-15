# Generated by Django 2.2 on 2021-07-15 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usage', '0003_auto_20210715_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerreading',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='customerreading', to='usage.Customer'),
        ),
        migrations.AlterField(
            model_name='customerreading',
            name='rate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='customerreading', to='usage.Rate'),
        ),
    ]
