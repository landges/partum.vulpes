# Generated by Django 3.2.6 on 2023-04-23 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20230301_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='dsc',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
