# Generated by Django 3.2.6 on 2023-01-31 11:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_index=True, max_length=64)),
                ('email', models.CharField(db_index=True, max_length=120)),
                ('phone', models.CharField(max_length=15)),
                ('content', models.TextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(default=datetime.datetime.now)),
                ('is_confirm', models.BooleanField(default=False)),
                ('is_pay', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('price', models.IntegerField()),
                ('time', models.IntegerField()),
                ('image', models.ImageField(upload_to='products/')),
            ],
        ),
        migrations.CreateModel(
            name='ProductInOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='web.order')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='web.product')),
            ],
        ),
    ]