# Generated by Django 4.0.1 on 2022-02-11 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_new_arrival_product_all_time_special_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tag',
        ),
    ]