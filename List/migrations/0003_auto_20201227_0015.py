# Generated by Django 3.1.4 on 2020-12-26 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('List', '0002_auto_20201226_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.CharField(default='', max_length=20),
        ),
    ]
