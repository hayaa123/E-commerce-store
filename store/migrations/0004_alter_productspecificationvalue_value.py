# Generated by Django 4.0.1 on 2022-02-01 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_productspecificationvalue_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productspecificationvalue',
            name='value',
            field=models.CharField(default='not available', max_length=225),
        ),
    ]
